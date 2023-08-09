from typing import BinaryIO
# 2022-07-30 ebb: We are altering this python script to handle inputs marked in a new way.
# ALL files have <note>...</note>
# Thomas edition has <add>....</add>, <del>....</del>,
# as well as <add-INNER>...</add-INNER> and <del-INNER>...</del-INNER>
# msColl edition has <sga-add sID="..""/> and <sga-add eID="..""/>: to be set in IGNORE list
# msColl edition has <del>...</del> and <del-INNER>...</del-INNER>
# msColl edition has <milestone unit="tei:p-START"/> and <milestone unit="tei:p-END"/>
# 2023-01-21: We have now prepared <head>...</head> elements that wrap chapter/letter/section headings as well.
# We now try to create very long tokens out of these to improve the collation alignments.
from collatex import *
from xml.dom import pulldom
import re
import glob
from datetime import datetime, date
import sys
import os

now = datetime.utcnow()
nowStr = str(now)

print('test: ', dir(Collation))
regexHyphen = re.compile(r'\S[\‑‒–—]\S')
regexWhitespace = re.compile(r'\s+')
regexNonWhitespace = re.compile(r'\S+')
regexEmptyTag = re.compile(r'/>$')
regexBlankLine = re.compile(r'\n{2,}')
regexLeadingBlankLine = re.compile(r'^\n')
regexPageBreak = re.compile(r'<pb.+?/>', re.DOTALL)
RE_MARKUP = re.compile(r'<.+?>', re.DOTALL)
RE_WORD_START = re.compile(r'<w ana="start"/>(.+)<lb[^<>]+>')
RE_WORD_END = re.compile(r'<w ana="end"/>')
# RE_HI_START = re.compile(r'<hi\ssID.+?/>')
# RE_HI_END = re.compile(r'<hi\seID.+?/>')
RE_PARASTART = re.compile(r'<p\ssID.+?/>')
RE_PARAEND = re.compile(r'<p\seID.+?/>')
RE_INCLUDE = re.compile(r'<include.*?/>')
RE_HEAD = re.compile(r'<head.*?/>')
RE_AB = re.compile(r'<ab.*?/>')
# 2018-10-1 ebb: ampersands are apparently not treated in python regex as entities any more than angle brackets.
# RE_AMP_NSB = re.compile(r'\S&amp;\s')
# RE_AMP_NSE = re.compile(r'\s&amp;\S')
# RE_AMP_SQUISH = re.compile(r'\S&amp;\S')
# RE_AMP = re.compile(r'\s&amp;\s')
RE_AMP = re.compile(r'&')
RE_LT_AMP = re.compile(r'&amp;')
# RE_MULTICAPS = re.compile(r'(?<=\W|\s|\>)[A-Z][A-Z]+[A-Z]*\s')
# RE_INNERCAPS = re.compile(r'(?<=hi\d"/>)[A-Z]+[A-Z]+[A-Z]+[A-Z]*')
# TITLE_MultiCaps = match(RE_MULTICAPS).lower()
# RE_NOTE = re.compile(r'<note[^<]*?>.+?</note>', re.MULTILINE | re.DOTALL)
# RE_DEL = re.compile(r'<del[^<\-]*?>.+?</del>', re.MULTILINE | re.DOTALL)
RE_ADDSTART = re.compile(r'<add[^<>]*?>')
RE_ADDEND = re.compile(r'</add>')
RE_NOTE_START = re.compile(r'<note[^<>]+?sID[^<>]+?>')
RE_NOTE_END = re.compile(r'<note[^<>]+?eID[^<>]+?>')
RE_DELSTART = re.compile(r'<del[^<>]*?>')
RE_DELEND = re.compile(r'</del>')
# 2023-05-17 ebb with nlh: We have altered the delSpans thus:
# <delSpan spanTo="id"/> as a start marker and a <delSpan anchor="id"/> in the pre-processed msColl for collation.
# Before the endpoints were <anchor> elements with only xml:ids,
# indistinguishable from the many other anchor elements in the msColl files.
# We want to make it possible for these to be seen in the normalized tokens used in the output collation.
# so they can be displayed as deleted passages in the variant panels.
RE_DELSPAN_START = re.compile(r'<delSpan[^<>]+?spanTo[^<>]+?/>')
RE_DELSPAN_END = re.compile(r'<delSpan[^<>]+?anchor[^<>]+?/>')

RE_ANCHOR = re.compile(r'<anchor.+?/>')
RE_SGA_ADDSTART = re.compile(r'<sga-add[^<>]+?sID[^<>]+?/>')
RE_SGA_ADDEND = re.compile(r'<sga-add[^<>]+?eID[^<>]+?/>')
RE_MDEL = re.compile(r'<mdel[^<>]*?>[^<>]+?</mdel>')
# RE_SHI = re.compile(r'<shi.*?>.+?</shi>')
RE_SHI_START = re.compile(r'<shi[^<>]*?>')
RE_SHI_END = re.compile(r'</shi>')
RE_METAMARK = re.compile(r'<metamark[^<>]*?>.+?</metamark>')
RE_HI = re.compile(r'<hi\s.+?/>')
RE_HI_START = re.compile(r'<hi\s*sID.+?>')
RE_HI_END = re.compile(r'<hi\s*eID.+?>')
RE_PB = re.compile(r'<pb.*?/>')
RE_SPACE_LB = re.compile(r'([\w\s])<lb.*?/>')
RE_LB = re.compile(r'<lb.*?/>')
# ebb: considered: re.DOTALL ? Probably don't need it b/c these regexes are being performed on tokens.
RE_LG = re.compile(r'<lg[^<]*/>')
RE_L = re.compile(r'<l\s[^<]*/>')
RE_CIT = re.compile(r'<cit\s[^<]*/>')
RE_QUOTE = re.compile(r'<quote\s[^<]*/>')
RE_OPENQT = re.compile(r'“')
RE_CLOSEQT = re.compile(r'”')
RE_GAP = re.compile(r'<gap\s[^<]*/>')
# &lt;milestone unit="tei:p"/&gt;
RE_sgaPSTART = re.compile(r'<milestone[^<]+?unit="tei:p-START.+?/>')
RE_sgaPEND = re.compile(r'<milestone[^<]+?unit="tei:p-END.+?/>')
RE_MILESTONE = re.compile(r'<milestone.+?>')
# 2022-07-16 amended 07-31 ebb: Milestone subbing is a special problem: In S-GA paragraphs
# are marked w/ milestone elements with @unit="tei:p"
# and also milestones are used for other things like "tei:seg""
# So we'll do a regex substitution for the paragraphs first, and THEN move to the other milestones.
RE_MOD = re.compile(r'<mod\s[^<]*/>')
RE_MULTI_LEFTANGLE = re.compile(r'<{2,}')
RE_MULTI_RIGHTANGLE = re.compile(r'>{2,}')
RE_LT_START = re.compile(r'<longToken.*?>')
RE_LT_END = re.compile(r'</longToken>')
RE_HEAD_START = re.compile(r'<head.*?>')
RE_HEAD_END = re.compile(r'</head>')
RE_DOTDASH = re.compile(r'\.–')
RE_BIBL = re.compile(r'<bibl.+?>') #Added 2023-07-09 ebb
RE_ZONE = re.compile(r'<zone.+?>') #Added 2023-07-30 ebb

# RE_DOTDASH captures a period followed by a dash, frequently seen in the S-GA edition, and not a word-dividing hyphen.
# 2022-08-08 ebb: I'm currently treating the "dotdash" as just a period for normalization to improve alignments.

# ebb: RE_MDEL = those pesky deletions of two letters or less that we want to normalize out of the collation, but preserve in the output.

# Element types: xml, div, head, p, hi, pb, note, lg, l; comment()
# Tags to ignore, with content to keep: xml, comment, anchor
# Structural elements: div, p, lg, l
# Inline elements (empty) retained in normalization: pb, milestone, xi:include
# Inline and block elements (with content) retained in normalization: note, hi, head, ab

# GIs fall into one three classes
# 2017-05-21 ebb: Due to trouble with pulldom parsing XML comments, I have converted these to comment elements,
# 2017-05-21 ebb: to be ignored during collation.
# 2017-05-30 ebb: Determined that comment elements cannot really be ignored when they have text nodes (the text is
# 2017-05-30 ebb: collated but the tags are not). Decision to make the comments into self-closing elements with text
# 2017-05-30 ebb: contents as attribute values, and content such as tags simplified to be legal attribute values.
# 2017-05-22 ebb: I've set anchor elements with @xml:ids to be the indicators of collation "chunks" to process together
ignore = ['sourceDoc', 'xml', 'comment', 'include', 'addSpan', 'handShift', 'damage', 'unclear', 'restore', 'surface', 'zone', 'retrace']
blockEmpty = ['p', 'div', 'milestone', 'lg', 'l', 'cit', 'quote', 'bibl']
inlineEmpty = ['mod', 'pb', 'sga-add', 'delSpan', 'anchor', 'lb', 'gap', 'hi', 'w', 'ab']
inlineContent = ['del-INNER', 'add-INNER', 'metamark', 'shi']
inlineVariationEvent = ['head', 'del', 'mdel', 'add', 'note', 'longToken']


# 10-23-2017 ebb rv:

def normalizeSpace(inText):
    """ Replaces all whitespace spans with a newline character for tokenization."""
    if regexNonWhitespace.search(inText):
        return regexWhitespace.sub('\n', inText)
    else:
        return ''


def extract(input_xml):
    """Process entire input XML document, firing on events"""
    # Start pulling; it continues automatically
    doc = pulldom.parse(input_xml)
    output = ''
    for event, node in doc:
        # elements to ignore: xml
        if event == pulldom.START_ELEMENT and node.localName in ignore:
            continue
        # copy comments intact
        # if event == pulldom.COMMENT:
        #     doc.expandNode(node)
        #     output += node.toxml()
        # ebb: The following handles our longToken and longToken-style elements:
        # complete element nodes surrounded by newline characters to make a long complete token:
        if event == pulldom.START_ELEMENT and node.localName in inlineVariationEvent:
            doc.expandNode(node)
            # 2022-10-25 ebb: The line above may be sending the characters inside the node to be processed twice,
            # resulting in the patterns of `&amp;&amp; for a single &amp; or &amp;&amp;quot; and andquot
            # output += '\n' + node.toxml() + '\n'
            # print(node.toxml()); Today, we cannot find a good pre-processing solution, but I hypothesize that
            # we might run this node.toxml() output through a sub function to do the equivalent of
            # the XSLT replace() we're now doing to handle this problem in post-processing.
            output += '\n' + node.toxml() + '\n'
            # output += '\n' + node.toxml()
        # ebb: Next (below): empty block elements: pb, milestone, lb, lg, l, p, ab, hi,
        # We COULD set white spaces around these like this ' ' + node.toxml() + ' '
        # but what seems to happen is that the white spaces get added to tokens; they aren't used to
        # isolate the markup into separate tokens, which is really what we'd want.
        # So, I'm removing the white spaces here.
        # NOTE: Removing the white space seems to improve/expand app alignment
        # 2022-07-16 ebb: With help from yxj, found that adding \n to each side of blockEmpty and inlineEmpty elements
        # stops the problem of forming tokens that fuse element tags to words.
        elif event == pulldom.START_ELEMENT and node.localName in blockEmpty:
            output += '\n' + node.toxml() + '\n'
        # ebb: empty inline elements that do not take surrounding white spaces:
        elif event == pulldom.START_ELEMENT and node.localName in inlineEmpty:
            output += node.toxml()
        # non-empty inline elements: mdel, shi, metamark
        elif event == pulldom.START_ELEMENT and node.localName in inlineContent:
            output += '\n' + regexEmptyTag.sub('>', node.toxml())
            # output += '\n' + node.toxml()
        elif event == pulldom.END_ELEMENT and node.localName in inlineContent:
            output += '</' + node.localName + '>' + '\n'
        # elif event == pulldom.START_ELEMENT and node.localName in blockElement:
        #    output += '\n<' + node.localName + '>\n'
        # elif event == pulldom.END_ELEMENT and node.localName in blockElement:
        #    output += '\n</' + node.localName + '>'
        elif event == pulldom.CHARACTERS:
            # output += fixToken(normalizeSpace(node.data))
            output += normalizeSpace(node.data)

        else:
            continue
    return output


# 2023-01-03 ebb: We created the fixToken function to make hyphens and dashes all be tokenized.
# Reviewing the collation outputs with and without the function in effect, the function does not seem
# to improve alignments: it splits up the collation into more app elements and is not as helpful as we
# thought at first.
# I'm commenting it out and removing the call to it in line 168 to determine
# whether there is any difference in the output:
# def fixToken(inText):
#     """ Add space before and after dash and hyphen """
#     fixToken = re.sub('(-|[‒–—])(\S)', '\n\\1\n\\2', inText)
#     fixToken = re.sub('(-|[‒–—])(\S)', '\n\\1\n\\2', fixToken)
#     fixToken = re.sub('(-|[‒–—])(\S)', '\n\\1\n\\2', fixToken)
#     return fixToken


def normalize(inputText):
    # 2022-07-16 ebb: Adding newlines here is too late: it just inserts a newline into a token.
    # 2022-08-06 ebb: I have rewritten this series of operations using a normalized variable for legibility.
    # These need to run in sequence: the order of replacements matters.
    # The lower() at the end lowercases all the normalized strings to simplify the comparison.

    normalized = RE_METAMARK.sub('', inputText)
    normalized = RE_MOD.sub('', normalized)
    # 2023-03-16 How about we actually read it this time? <mod> is in the ignore list like anchor, etc, so why are we presuming it's being read?
    normalized = RE_GAP.sub('', normalized)
    normalized = RE_CLOSEQT.sub('"', normalized)
    normalized = RE_OPENQT.sub('"', normalized)
    normalized = RE_QUOTE.sub('', normalized)
    normalized = RE_CIT.sub('', normalized)
    normalized = RE_BIBL.sub('', normalized) # Added 2023-07-29 ebb
    normalized = RE_L.sub('<l/>', normalized)
    normalized = RE_LG.sub('<lg/>', normalized)
    normalized = RE_AB.sub('', normalized)
    # 2022-08-06 <ab> wraps headings or starts of letters in the print editions
    normalized = RE_PARASTART.sub('<p-start/>', normalized)
    normalized = RE_PARAEND.sub('<p-end/>', normalized)
    normalized = RE_sgaPSTART.sub('<p-start/>', normalized)
    normalized = RE_sgaPEND.sub('<p-end/>', normalized)
    normalized = RE_MILESTONE.sub('', normalized)
    normalized = RE_PB.sub('', normalized)
    # 2023-05-17 ebb with nlh: Noting that delSpan needs a way to be expressed
    # in the output normalized tokens for the new interface.
    # Freshly altered delSpan and anchor in msColl files to delspan...delspan, normalizing in next two lines:
    normalized = RE_DELSPAN_START.sub('<del>', normalized)
    normalized = RE_DELSPAN_END.sub('</del>', normalized)
    normalized = RE_ANCHOR.sub('', normalized)
    normalized = RE_LT_AMP.sub('and', normalized)
    normalized = RE_AMP.sub('and', normalized)
    normalized = RE_WORD_START.sub(' \\1', normalized)
    # 2023-05-22 ebb and yxj: We must replace WORD_START before the SPACE_LB.
    # WORD_START replacement ensures that the normalized token for <w ana='start'/>...<lb/>...<w ana="end"/>
    # does not get an added space. We need to ensure that these are treated as single word tokens
    # with no space added internally.
    normalized = RE_WORD_END.sub(' ', normalized)
    normalized = RE_SPACE_LB.sub('\\1 ', normalized)
    normalized = RE_LB.sub('', normalized)
    normalized = RE_ZONE.sub('', normalized)
    normalized = RE_NOTE_START.sub('<note>', normalized)
    normalized = RE_NOTE_END.sub('</note>', normalized)
    normalized = RE_SGA_ADDSTART.sub('', normalized)
    normalized = RE_SGA_ADDEND.sub('', normalized)
    normalized = RE_ADDSTART.sub('', normalized)
    normalized = RE_ADDEND.sub('', normalized)
    normalized = RE_DELSTART.sub('<del>', normalized)
    normalized = RE_DELEND.sub('</del>', normalized)
    normalized = RE_LT_START.sub('', normalized)
    normalized = RE_LT_END.sub('', normalized)
    normalized = RE_HEAD_START.sub('', normalized)
    normalized = RE_HEAD_END.sub('', normalized)
    # 2023-06-30 nlh: added space inside <hi/> normalization.
    normalized = RE_HI_START.sub('<hi>', normalized) # ebb: 2023-07-30 We used to normalize <hi> as a space, but we're going to try supplying it as a start and end tag for the normalized tokens now.
    normalized = RE_HI_END.sub('</hi>', normalized)
    # 2022-08-08 ebb: Sometimes <hi> in the print editions seems irrelevant, in highlighting words at
    # chapter beginnings. However, it also sometimes indicates emphasis on a word.
    # Example: one or two little <hi sID="xxx"/>wives<hi eID="novel1_letter4_chapter6_div4_div6_p9_hi1"/>
    # On analysis of <hi> and <shi> in the print and SG-A editions, it is difficult to distinguish
    # meaningful highlights from conventional superscripts/underlining, so it seems best to ignore it in normalization,
    # or return to the source texts and add markup to distinguish passages giving emphasis.
    #  normalized = RE_SHI.sub('', normalized)
    normalized = RE_SHI_START.sub('', normalized)
    normalized = RE_SHI_END.sub('', normalized)
    # 2022-08-08 ebb: <shi> elements mark briefly highlighted words or passages in the S-GA edition.
    # The highlights themselves are not usually significant, but the text inside must be preserved for comparison.
    # Example: <shi rend="underline">should be</shi>
    # Previously, we were eliminating these passages entirely from the normalization, which was a serious error!
    # We have not been considering highlighting or emphasis <hi> or <shi> as a significant difference in the normalization.
    # 2023-03-16 ebb: We have moved mdel to inlineVariationEvent, and do not want to normalize its token, so we are commenting out the next line.
    # normalized = RE_MDEL.sub('', normalized)
    # 2022-08-08 ebb: <mdel> elements are tiny struck-out characters in the S-GA edition.
    # We do not think these are significant for comparison with the other editions, so we normalize them out.
    normalized = RE_DOTDASH.sub('. ', normalized)
    normalized = RE_INCLUDE.sub('', normalized)
    normalized = RE_MULTI_RIGHTANGLE.sub('>', normalized)
    normalized = RE_MULTI_LEFTANGLE.sub('<', normalized)
    normalized = re.sub(r'^\s+', '', normalized) # 2023-06-26 yxj: remvoe the space at the beginning
    normalized = re.sub(r'\s+$', '', normalized) # 2023-06-26 yxj: remvoe the space at the end
    normalized = normalized.lower()
    return normalized


def processToken(inputText):
    return {"t": inputText + ' ', "n": normalize(inputText)}


def processWitness(inputWitness, id):
    return {'id': id, 'tokens': [processToken(token) for token in inputWitness]}


def tokenize(inputFile):
    return regexLeadingBlankLine.sub('\n', regexBlankLine.sub('\n', extract(inputFile))).split('\n')

def tokenizeFiles(f1818, f1823, fThomas, f1831, fMS):
    with open(f1818, 'rb') as f1818file, \
            open(f1823, 'rb') as f1823file, \
            open(fThomas, 'rb') as fThomasfile, \
            open(f1831, 'rb') as f1831file, \
            open(fMS, 'rb') as fMSfile:
        f1818_tokenlist = processWitness(tokenize(f1818file), 'f1818')
        fThomas_tokenlist = processWitness(tokenize(fThomasfile), 'fThomas')
        f1823_tokenlist = processWitness(tokenize(f1823file), 'f1823')
        f1831_tokenlist = processWitness(tokenize(f1831file), 'f1831')
        fMS_tokenlist = processWitness(tokenize(fMSfile), 'fMS')
        return [f1818_tokenlist, f1823_tokenlist, fThomas_tokenlist, f1831_tokenlist, fMS_tokenlist]
def main():
    chunk = sys.argv[1]
    # chunk = 'C21'
    for f1818 in glob.glob('../collationChunks/' + chunk + '/input/1818_fullFlat_*'):
        try:
            collChunk = f1818.split("fullFlat_", 1)[1]
                # ebb: above gets C30.xml for example
                # matchStr = matchString.split(".", 1)[0]
                # ebb: above strips off the file extension

            f1823 = '../collationChunks/' + chunk + '/input/1823_fullFlat_' + collChunk
            fThomas = '../collationChunks/' + chunk + '/input/Thomas_fullFlat_' + collChunk
            f1831 = '../collationChunks/' + chunk + '/input/1831_fullFlat_' + collChunk
            fMS = '../collationChunks/' + chunk + '/input/msColl_' + collChunk
            # 2023-05-17 ebb: **Before we begin the tokenizing**, run a XSLT pre-processing pass:
            # Revise delSpan anchor elements and remove newlines from inlineVariationEvent elements so these hold together as long tokens:

            tokenLists = tokenizeFiles(f1818, f1823, fThomas, f1831, fMS)
            print(tokenLists)
            # 2022-11-14 yxj: For easier doing unit testing,
            # can we import 4 filenames instead of only 1 into tokenizeFiles()?

            collation_input = {"witnesses": tokenLists}
            outputFile = open('../collationChunks/' + chunk + '/output/Collation_' + chunk + '-partway.xml', 'w', encoding='utf-8')
                
            # table = collate(collation_input, output='tei', segmentation=True)
            # table = collate(collation_input, segmentation=True, layout='vertical')
            table = collate(collation_input, output='xml', segmentation=True)
            print(table + '<!-- ' + nowStr + ' -->', file=outputFile)
            # print(table + '<!-- ' + nowStr + ' -->')
            outputFile.close()

        except IOError:
            pass
main()