# Notes:

## 1-27-2023:

* Divergence in 1831 found: need to find starting point, but it's prominent around line 763.

* Simultaneous divergence found in Thomas in line 547. Monitor carefully, changes may not be necessary to Thomas.

## 1-30-2023

* After pretty printing, 1831 starts to diverge around line 473 and continues until line 665. 

* Lines 686 to 699 diverge for 1831, debating if it is too brief to make a longToken for.

* Possible divergence for 1831 spotted at line 772. Next time 1831 appears, some common words are shared, but there are a lot of different phrases and the divergence stops at line 1069.

* After previous note, no divergence until at least line 3000

## 2-1-2023

* **Mental Note:** Search for a phrase rather than a line number when writing up divergences. Pretty print and shell script will cause the numbers to change.

* Have the texts open for side-by-side comparison when planting long tokens.

* Carefully evaluate the manuscript to find long tokens.

* Take note of minor divergences/stacking issues in the manuscript. May be significant.

* Ending point: "Contempt - Devil"

## 2-8-2023

* Manuscript has issues aligning "Dust and Oh." Possibly too short for a longToken.

* Note: reposition longToken for "be calm" in MS

* Finishing Point: "and said- Be calm!"

## 2-12-23

* Trying to adjust the longToken for "and said - be calm!" so it aligns with teh rest of the text in the manuscript. Next note will describe if it works.

* Update: It didn't work. I'm wondering if I have to put the phrase in longTokens across the all the drafts in order for it to align, but I'll wait for evaluation.

* MS: "Although it be only an accumulation of anguish," "be" is detected in every draft except this one. The word is there, don't know why it wasn't detected.

* MS Confusion: The manuscript has "do not be equitable" while every other version has "be not equitable" MS has different word order, but "not" and "be" are isolated from the other drafts. Can't tell if it's supposed to be this way.

* MS: Clemency from "thy clemency and affection". Clemency is grouped with thy rather than with affection. Full statement may be "They clemency, thy affection," But I'm not certain and a misalignment may be possible here.

* MS: "Begone replied I-" properly aligned, but has extra words. Statements afterwards align properly, but write it down anyway. The same applies for "You? said the fiend;" properly aligned, just extra words.

* MS: "Mankind knew of my existence, they would do as you do." First "do" is missing in collation despite the phrase being identical in the MS.

* "Bloody as they are" (1823 + 1831), "Bloody as they may be" (1818 + Thomas), "Bloody as they be" (MS). Double-check realignment, token may be necessary. 

* Confusing alignment for a section including remembrance and circumstances. 

* Final note: read through section! Aside from today's notes, not too much revision appears to be necessary.

### 2023-02-12 ebb Review Comments
Reviewing the output, I'm adding several adjustments:

- [x] "My father was pleased, and Elizabeth overjoyed.": msColl is breaking up the alignment due to punctuation changes in a passage revised via Thomas.
Attempting to improve alignment by setting a longToken here:

```xml
 <longToken>My <w ana="start"/>fa<lb n="c56-0119__main__17"/>ther<w ana="end"/> was pleased and Elizabeth overjoyed;</longToken>
``` 

- [x] "summits of the mountains" passage: "the mountains," is pulled out of context in 1831, just before a lengthy longToken passage.
I'm attempting to set the lengthy longToken passage a little earlier to start around "the mountains, "

     * stretched the same 1831 longToken one word further to include the "and" before I resolved--it's misaligned. 
- [x] MSColl has deleted: "tranquillizing the" followed by "solemnizing" : Other editions have just "tranquillizing" and 1831 spells it "tranquillising".
This is coming out splitting in two app elements rather than one, so we can try to align them. 
I am wrapping a longToken around the MSColl deletion and insertion to see if that will align the editions in one app.

- [x] MSColl: adjusted "terrifical <lb/> ly" to set these on one line and remove the space (it's not different from the other editions here)

- [x] MSColl: added space before `<zone>` element to split up "leaningupon" ,(Fixed by adding another newline.)
- [x] MSColl: adjusted spacing for "the opposite mountain is a bare perpendicular" passage
- [x] multiple witnesses messed up (1823 w/ pb element): "dependent mountains"
- [x] MSColl: adjusted spacing here to unite parts of word: `approached seem<lb n="c56-0123__main__25"/>ed`
- [x] MSColl: parenthetical passage: "sight tremendous and" : added longToken like this:
`<longToken>(<del rend="strikethrough" xml:id="c56-0124__main__d5e25745">oh</del> sight tremendous and abhorred)</longToken>`
- [x] MSColl: need to split alignment: added longToken: `<longToken>this–</longToken> anger`
- [x] "rather stay,": 1831 and msColl split off in separate app. Added longToken to 1831: `<longToken>rather, stay,</longToken>` (Fixed after adding another longToken in msColl.)
- [x] MSColl: add space to unfuse `&the`: `&amp; <lb n="c56-0125__main__7"/> the`
- [x] MSColl: `<longToken>clemency, thy affection</longToken>`
- [x] MSColl: added space to split up fused token: `with&lt;lb n="c56-0127__main__1"/&gt;love`
- [x] Odd 1823 and 1831 alignment adds "I rejoined": `remembrance,” I rejoined, “circumstances,` 
while other editions have `remembrance circumstances`  and it's splitting across two apps badly. (Fixed by adding longTokens around the other editions here, with all longTokens including "circumstances".
Trying a longToken in both 1823 and 1831 here: `<longToken>remembrance,” I rejoined,</longToken>`
- [x] MSColl: split up fused token around `the&lt;lb n="c56-0129__main__1"/&gt;heavens –`
- [x] MSColl: split up fused token around `heavy&lt;lb n="c56-0130__main__1"/&gt;heart`
