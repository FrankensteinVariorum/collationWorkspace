from ClusterShell.RangeSet import RangeSet
from collatex.block import Block
from collatex.core_classes import Token
from collatex.linsuffarr import SuffixArray
from collatex.linsuffarr import UNIT_BYTE


class Stack(list):
    def push(self, item):
        self.append(item)

    def peek(self):
        return self[-1]


# TokenIndex
class TokenIndex(object):
    def __init__(self, witnesses):
        self.witnesses = witnesses
        # print("\nwitnesses=",witnesses)
        self.counter = 0
        self.witness_ranges = {}
        self.token_array = []
        self.witness_to_block_instances = {}
        self.suffix_array = []
        self.lcp_array = []
        self.blocks = []

    def prepare(self):
        self._prepare_token_array()
        # print("> self.token_array=", self.token_array)
        # call third party library here
        self.suffix_array = self.get_suffix_array()
        self.lcp_array = self.get_lcp_array()
        self.blocks = self.split_lcp_array_into_intervals()
        self.construct_witness_to_block_instances_map()

    @classmethod
    def create_token_index(cls, collation):
        token_index = TokenIndex(collation.witnesses)
        token_index.prepare()
        return token_index

    def _prepare_token_array(self):
        # TODO: the lazy init should move to somewhere else
        # clear the suffix array and LCP array cache
        self.cached_suffix_array = None
        token_array_position = 0
        for idx, witness in enumerate(self.witnesses):
            # print("witness.tokens",witness.tokens())
            witness_range = RangeSet()
            witness_range.add_range(self.counter, self.counter + len(witness.tokens()))
            # the extra one is for the marker token
            self.counter += len(witness.tokens()) + 1
            self.witness_ranges[witness.sigil] = witness_range
            # remember get tokens twice
            sigil = witness.sigil
            for token in witness.tokens():
                token.token_data['_sigil'] = sigil
                token.token_data['_token_array_position'] = token_array_position
                token_array_position += 1
            self.token_array.extend(witness.tokens())
            # # add marker token
            self.token_array.append(Token({"n": '$' + str(idx), '_sigil': sigil}))
            token_array_position += 1
        self.token_array.pop()  # remove last marker

    def split_lcp_array_into_intervals(self):
        closed_intervals = []
        previous_lcp_value = 0
        open_intervals = Stack()
        for idx in range(0, len(self.lcp_array)):
            lcp_value = self.lcp_array[idx]
            if lcp_value > previous_lcp_value:
                open_intervals.push(Block(self, start=idx - 1, length=lcp_value))
                previous_lcp_value = lcp_value
            elif lcp_value < previous_lcp_value:
                #         close open intervals that are larger than current LCP value
                while open_intervals and open_intervals.peek().length > lcp_value:
                    a = open_intervals.pop()
                    closed_intervals.append(Block(self, start=a.start, end=idx - 1, length=a.length))

                # then: open a new interval starting with filtered intervals
                if lcp_value > 0:
                    start = closed_intervals[len(closed_intervals) - 1].start
                    open_intervals.push(Block(self, start=start, length=lcp_value))

                previous_lcp_value = lcp_value

        # add all the open intervals to the result
        # print("> open_intervals=", open_intervals)
        # print("> closed_intervals=", closed_intervals)
        for interval in open_intervals:
            if interval.length > 0:
                closed_intervals.append(
                    Block(self, start=interval.start, end=len(self.lcp_array) - 1, length=interval.length))
        # print("> closed_intervals=", closed_intervals)
        return closed_intervals

    def get_range_for_witness(self, witness_sigil):
        if witness_sigil not in self.witness_ranges:
            raise Exception("Witness " + witness_sigil + " is not added to the collation!")
        return self.witness_ranges[witness_sigil]

    def get_sa(self):
        # NOTE: implemented in a lazy manner, since calculation of the Suffix Array and LCP Array takes time
        # print("token_array=",self.token_array)
        # for token in self.token_array:
        #     print(token,":",type(token))
        if not self.cached_suffix_array:
            # string_array = ''.join([token.token_string for token in self.token_array])
            string_array = [token.token_string for token in self.token_array]
            # Unit byte is done to skip tokenization in third party library
            ##print("> string_array =", string_array)
            self.cached_suffix_array = SuffixArray(string_array, unit=UNIT_BYTE)
            ##print("> suffix_array:\n", self.cached_suffix_array)
        return self.cached_suffix_array

    def get_suffix_array(self):
        sa = self.get_sa()
        return sa.SA

    def get_lcp_array(self):
        sa = self.get_sa()
        return sa._LCP_values

    def start_token_position_for_witness(self, witness):
        return self.get_range_for_witness(witness.sigil)[0]

    def block_instances_for_witness(self, witness):
        return self.witness_to_block_instances.setdefault(witness.sigil, [])

    def construct_witness_to_block_instances_map(self):
        self.witness_to_block_instances = {}
        ##print("> self.blocks", self.blocks)
        for interval in self.blocks:
            for instance in interval.get_all_instances():
                ##print(">instance = ", instance)
                w = instance.get_witness_sigil()
                instances = self.witness_to_block_instances.setdefault(w, [])
                instances.append(instance)

    # # NOTE: LCP intervals can 1) ascend or 2) descend or 3) first ascend and then descend. 4) descend, ascend
    # def split_lcp_array_into_intervals(self):
    #     closed_intervals = []
    #     previous_lcp_value = 0
    #     open_intervals = Stack()
    #     for idx, lcp_value in enumerate(self.lcp_array):
    #         #             print(lcp_value)
    #         if lcp_value > previous_lcp_value:
    #             open_intervals.push((idx - 1, lcp_value))
    #             previous_lcp_value = lcp_value
    #         if lcp_value < previous_lcp_value:
    #             # close open intervals that are larger than current lcp_value
    #             while open_intervals and open_intervals.peek()[1] > lcp_value:
    #                 #                     print("Peek: "+str(open_intervals.peek()))
    #                 (start, length) = open_intervals.pop()
    #                 # TODO: FIX NUMBER OF SIBLINGS!
    #                 closed_intervals.append(LCPInterval(self, start, idx - 1, length, 0))
    #                 #                     print("new: "+repr(closed_intervals[-1]))
    #             # then: open a new interval starting with start filter open intervals.
    #             if lcp_value > 0:
    #                 start = closed_intervals[-1].start
    #                 open_intervals.push((start, lcp_value))
    #             previous_lcp_value = lcp_value
    #     # add all the open intervals to the result
    #     #         print("Closing remaining:")
    #     for start, length in open_intervals:
    #         # TODO: FIX NUMBER OF SIBLINGS!
    #         closed_intervals.append(LCPInterval(self, start, len(self.lcp_array) - 1, length, 0))
    #         #             print("new: "+repr(closed_intervals[-1]))
    #     return closed_intervals

    # factory method for testing purposes only!
    @classmethod
    def for_test(cls, sa_array, lcp_array):
        token_index = TokenIndex(None)
        token_index.suffix_array = sa_array
        token_index.lcp_array = lcp_array
        return token_index  # parts of the LCP array become potential blocks.

# # minimum block_length: the number of tokens a single occurrence of this block spans
# # block_occurrences: the ranges within the suffix array that this block spans
# class LCPInterval(object):
#     def __init__(self, token_index, start, end, length, number_of_siblings):
#         self.token_index = token_index
#         self.start = start
#         self.end = end
#         self.length = length
#         self.number_of_siblings = number_of_siblings
#
#     @property
#     def minimum_block_length(self):
#         return self.length
#
#     @property
#     def number_of_occurrences(self):
#         return self.end - self.start + 1
#
#     def block_occurrences(self):
#         block_occurrences = []
#         for idx in range(self.start, self.end + 1):
#             block_occurrences.append(self.token_index.suffix_array[idx])
#         return block_occurrences
#
#     def info(self):
#         return "looking at: " + str(self)
#
#     @property
#     def token_start_position(self):
#         return min(self.block_occurrences())
#
#     def _as_range(self):
#         # convert interval into range
#         range_set = RangeSet()
#         for occurrence in self.block_occurrences():
#             range_set.add_range(occurrence, occurrence + self.minimum_block_length)
#         return range_set
#
#     @property
#     def number_of_witnesses(self):
#         range = self._as_range()
#         number_of_witnesses = 0
#         for witness_range in self.token_index.witness_ranges.values():
#             if witness_range.intersection(range):
#                 number_of_witnesses += 1
#         return number_of_witnesses
#
#     def show_lcp_array(self):
#         return self.LCP[self.start:self.end + 1]
#
#     def __lt__(self, other):
#         same = other.number_of_witnesses == self.number_of_witnesses
#         if not same:
#             return other.number_of_witnesses < self.number_of_witnesses
#
#         same = other.length == self.length
#         if not same:
#             return other.length < self.length
#
#         return self.number_of_occurrences < other.number_of_occurrences
#
#     def __str__(self):
#         tokens = (token.token_string for token in self.token_index.token_array[
#                                                   self.token_index.suffix_array[self.start]:
#                                                   self.token_index.suffix_array[self.start] + min(10,
#                                                                                                   self.minimum_block_length)])
#         part1 = "<" + " ".join(tokens)
#         return part1 + "> with " + str(self.number_of_witnesses) + ":" + str(
#             self.number_of_occurrences) + " witnesses/occurrences and length: " + str(
#             self.minimum_block_length) + " and number of siblings: " + str(self.number_of_siblings)
#
#     # start (suffix), length, depth, frequency
#     def __repr__(self):
#         return "LCPivl: " + str(self.start) + "," + str(self.minimum_block_length) + "," + str(
#             self.number_of_witnesses) + "," + str(self.number_of_occurrences)
