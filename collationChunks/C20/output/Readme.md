# 3-1-2023

- [X] Setting up branch!

- [X] Adding longToken for MS Chapter
- [ ] Problem aligning around first word of chapter. MS has "Sometime", others have "Some time".
   MS "Sometime" is aligned wrongly around the Chapter longToken. We attempted to place `<longToken>` around the "Sometime elapsed before I" passages across all texts, and it made things worse.
   

# 3-7-2023

- [X] MS: "interesting and wonderful" is sorted as `inter`, `esting`, `andwonderful`. "And wonderful" can possibly be split up, but "inter" has a delete tag between it and "esting," may not be fixable.
- [X] MS: Spacing fix possible: `andagatha`
- [X] MS: Spacing fix possible: `andluxurious`
- [X] MS: Spacing fix possible: `['relig', '&lt;delstart/&gt;i&lt;delend/&gt;', 'ion']` into "religion"
- [X] MS: Spacing fix possible: `['in', 'dignation', '', '', 'w', '', 'ere', '', 'uncontrolable']`
- [X] Alignment Question: all the passages have the phrase `['and', 'then', 'looked', 'around', 'for', 'the', 'means.', 'after', 'many', 'fruitless', 'attempts', 'to', 'gain', 'admittance', 'to', 'the']`, but the phrase ends with `Prison`, which is its own separate reading group/app. Should they be combined to complete the phrase?
- [X] MS: Spacing fix possible: `['st', '', '', 'r', '', 'ongly']`
- [X] MS: Spacing fix possible: `['know', 'n', '']`
- [X] MS: an area is aligned properly, but the MS is a massive text jumble (see below). May possibly need fixing.

`<rdg wit="fMS">&lt;sga-add place="sublinear" sID="c57-0032__main__d4e5325"/&gt;
			&lt;metamark function="insert"&gt;^&lt;/metamark&gt; &lt;sga-add
			eID="c57-0032__main__d4e5325"/&gt; &lt;del rend="strikethrough"
			xml:id="c57-0032__main__d4e5331"&gt; &lt;sga-add hand="#pbs" place="superlinear"
			sID="c57-0032__main__d4e5333"/&gt;altho it had not en &lt;sga-add
			eID="c57-0032__main__d4e5333"/&gt; &lt;/del&gt; would fully reward his &lt;lb
			n="c57-0032__main__27"/&gt;toil &amp; hazard. &lt;milestone unit="tei:p-END"/&gt;
			&lt;milestone unit="tei:p-START"/&gt;</rdg>`
 - [ ] MS: **Misalignment detected!** "onheart of Felix" in the MS is different from the other passages, where it appears a few reading groups later. May be the result of "on" and "heart" being combined, but when "heart of Felix" shows up for the other passages, MS has "Full Zeal" in the same reading group. Not 100% sure about this one.

 - [ ] MS: Possible divergence, as "The Turk informed Safie has more going on in the MS, but it is not written and the MS disappears for several passages, only appearing in three of the next several: "of", "his". "intentions". It begins getting complicated after this.
 - [ ]  MS: "Rank" is included in the same reading group as "across mont cenis to leghorn, where", but the mont is never mentioned in MS. Should it be isolated?
 - [ ] MS: Appears in a reading group with a blank token for a second time during this section: `['with', 'him', 'when', 'he', 'departed.', 'his', 'plans', 'were']`
 -  **Side Note:** MS once again disappears after the blank token and reappears starting at "to think no more of"
 - [ ] MS: Spacing fix possible: `himto`	
 - [X] MS: Text jumble detected: `['', '&lt;delstart/&gt;lef&lt;delend/&gt;', '&lt;delstart/&gt;deserted by her father&lt;delend/&gt;']`

# 3-8-2023
 - [ ] MS: Has a passage `fathers that` while 1823 and 1831 have `father` and both 1818 and Thomas have `Father's` The next reading group has `which`, so I'm thinking `that` from the MS should be in the same reading group as `which`   
 - [ ] MS: Spacing fix possible, but maybe unnecessary: `['a', 'n', '', '&lt;delstart/&gt;servant who&lt;delend/&gt;', 'attendant']`
 - [ ] MS: Spacing fix possible: `['tur', 'kish', 'arabic', '']`
 - [ ] All passages: there are two sections that may need altering: `leagues from the cottage of De` and `Lacey, when`. Should De Lacey be in the same statement? 
 - [ ] MS: at the end, "Lover" is mentioned twice in two subsequent reading groups: `her lover`, `lover in his retreat`. Should anything be altered? This feels redundant, or possibly a mistake slipped through.
 - **Finishing Point:** End of Chapter

# 3-15-2023 
 - [ ] All editions: `Some time` vs `Sometime` at the start of the chapter is a tricky fix. **Decision to do manually.**
 - [ ] **Fix "Condemnation" manually**
 - [X] Possible divergence: MS disappears after "consummation of his happiness" and shows up again for a milestone unit before reappearing fully starting with "The Turk." Should any action be taken? **Would have to add longToken to all 5 editions**
 - [ ] MS stops briefly after "The commander", but the other four readings have lengthy blocks of text, with the MS reappearing starting with "his daughter." Should something be done about this? **Yes, Check the Paragraph alignment, put longTokens in all editions**
  - [ ] Alignment question: all categories end with "Felix Had" at one point, but 1823 and 1831 include the word "accidentally" before converging with every category (except the manuscript) at "been." Debating is they should stay as-is.
  - [ ] MS: `['government–', 'he', 'had', 'just', 'heard', 'of', 'a', 'small', 'vessel', 'bound', 'for', 'constantinople', 'which']` is all grouped together, but many elements from this string appear in separated reading groups. This may need fixing, but I'm skeptical because the same text appears in those reading groups. 
  - [x] MS: For "in his interests", it has a blank token and no text. Why is that there? **ebb: repaired: we were correct to realign and remove the empty token**

  # 3-22-2023
  - [ ] left a long token for "full zeal." run shell script.

 # 3-23-2023
 - [ ] Tried resolving "On heart of Felix" issue with the Manuscript, but I don't think I solved it. May need to be fixed manually
 - **Side Notes:** MS only has "Heart of Felix" once, every other version has it occur twice. In the versions wrapped in longTokens, some were punctuated and some were not. Running the script a second time to see if isolating the punctuation fixes anything.
 - **Possibly Fixed!** The Manuscript shows up with the others, but other adjustments have followed it afterwards. Assess this before marking as fixed. 
 - **Sending this branch for review:** Dr. Bondar can give this a look, and hopefully there are very few issues left. I will switch to main branch and create a branch for C22 now and make chapters into longTokens if necessary.

# 7-09-2023

- [ ] Merge apps: wrapping longToken around `learnt the name of the spot where he then` in print editions.