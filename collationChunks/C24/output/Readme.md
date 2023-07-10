# 4-12-2023
- Establishing branch and running collation for the first time

# 4-14-2023

- [x] **Confusion** In the first `<app>`, the Chapter for the MS is listed. Shouldn't it be in the second app? 

```
<app>
		<rdgGrp n="['']">
			<rdg wit="f1818">&lt;milestone unit="chapter" type="start" n="17"/&gt;</rdg>
			<rdg wit="f1823">&lt;pb xml:id="F1823_v2_362" n="89"/&gt;</rdg>
			<rdg wit="fThomas">&lt;milestone unit="chapter" type="start" n="17"/&gt;</rdg>
			<rdg wit="f1831">&lt;milestone unit="chapter" type="start" n="18"/&gt;</rdg>
		</rdgGrp>
		<rdgGrp n="['chap.', '10', 'th']">
			<rdg wit="fMS">Chap. 10 &lt;shi rend="underline"&gt;th&lt;/shi&gt;</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['chapter i.']">
			<rdg wit="f1818">&lt;head&gt;CHAPTER I.&lt;/head&gt;</rdg>
			<rdg wit="fThomas">&lt;head&gt;CHAPTER I.&lt;/head&gt;</rdg>
		</rdgGrp>
		<rdgGrp n="['chapter vi.']">
			<rdg wit="f1823">&lt;head&gt;CHAPTER VI.&lt;/head&gt;</rdg>
		</rdgGrp>
		<rdgGrp n="['chapter xviii.']">
			<rdg wit="f1831">&lt;head&gt;CHAPTER XVIII.&lt;/head&gt;</rdg>
		</rdgGrp>
```
- [x] **Confusion:** For "I was unable to overcome my repugnance", I found a similar phrase in the MS, yet it was not detected by the script. It may have been a deletion, needs evaluation.

```
<app>
		<rdgGrp
			n="['i', 'was', 'unable', 'to', 'overcome', 'my', 'repugnance', 'to', 'the', 'task', 'which', 'was', 'enjoined', 'me.', 'i', 'found', 'that']">
			<rdg wit="f1818">I was unable to overcome my repugnance to the task which was enjoined
				me. I found that</rdg>
			<rdg wit="f1823">I was unable to overcome my repugnance to the task which was enjoined
				me. I found that</rdg>
			<rdg wit="fThomas">I was unable to overcome my repugnance to the task which was enjoined
				me. I found that</rdg>
			<rdg wit="f1831">I was unable to overcome my repugnance to the task which was enjoined
				me. I found that</rdg>
		</rdgGrp>
```

- [x] **Misalignment Detected:** The manuscript's phrase of "I was unable to overcome my repugnance" comes later than every other edition, possibly due to word order in the drafts. The MS disappears at several points (indicating that the MS did not contain certain passages), but there is a lot of overlap where it shouldn't be, more than I can copy and paste.

- [x] **Confusion:** MS has the phrase "alone in a little boat" appear about two apps sooner than when it appears in other editions, yet the passage before it appears well aligned. I'll post the cope snippets, but something isn't right.

```
<app>
		<rdgGrp n="['solitude.']">
			<rdg wit="f1818">solitude.</rdg>
			<rdg wit="f1823">solitude.</rdg>
			<rdg wit="fThomas">solitude.</rdg>
			<rdg wit="f1831">solitude.</rdg>
		</rdgGrp>
		<rdgGrp
			n="['solitude:', '&lt;delstart/&gt;and my deli&lt;delend/&gt;', '&lt;delstart/&gt;i used to&lt;delend/&gt;', '', 'alone', 'in', 'a', 'little', 'boat', '', '']">
			<rdg wit="fMS">solitude: &lt;del rend="strikethrough"
				xml:id="c57-0074__main__d4e14584"&gt;&amp; my deli&lt;/del&gt; &lt;del
				rend="strikethrough" xml:id="c57-0074__main__d4e14587"&gt;I used to&lt;/del&gt;
				&lt;milestone spanTo="#c57-0074.02" unit="tei:seg" xml:id="c57-0074.03"/&gt; Alone
				&lt;lb n="c57-0074__main__19"/&gt;in a little boat &lt;anchor
				xml:id="c57-0074.02"/&gt; &lt;milestone spanTo="#c57-0074.04" unit="tei:seg"
				xml:id="c57-0074.05"/&gt;</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['i', 'passed', 'whole', 'days', 'on', 'the', 'lake']">
			<rdg wit="f1818">I passed whole &lt;pb xml:id="F1818_v3_007" n="003"/&gt;days on the
				lake</rdg>
			<rdg wit="f1823">I passed whole days on the lake</rdg>
			<rdg wit="fThomas">I passed whole &lt;pb xml:id="F1818_v3_007" n="003"/&gt;days on the
				lake</rdg>
			<rdg wit="f1831">I passed whole days on the lake</rdg>
			<rdg wit="fMS">I passed whole days on &lt;lb n="c57-0074__main__20"/&gt;the lake</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['']">
			<rdg wit="fMS">&lt;anchor xml:id="c57-0074.04"/&gt;</rdg>
		</rdgGrp>
		<rdgGrp n="['alone', 'in', 'a', 'little', 'boat,']">
			<rdg wit="f1818">alone in a little boat,</rdg>
			<rdg wit="f1823">alone in a little boat,</rdg>
			<rdg wit="fThomas">alone in a little boat,</rdg>
			<rdg wit="f1831">alone in a little boat,</rdg>
		</rdgGrp>
	</app>
```

- [x] **Confusion:** What's going on here?

```
<app>
		<rdgGrp
			n="['', '', '&lt;metamark function=&#34;displacement&#34;&gt;my', 'repugnance)x&lt;/metamark&gt;', 'i', 'found', 'also', '', 'that']">
			<rdg wit="fMS">&lt;metamark function="sequence"&gt;1&lt;/metamark&gt; &lt;lb
				n="c57-0075__main__2"/&gt; &lt;metamark function="displacement"&gt;my
				repugnance)X&lt;/metamark&gt; I found &lt;sga-add place="superlinear"
				sID="c57-0075__main__d4e14739"/&gt;also &lt;sga-add
				eID="c57-0075__main__d4e14739"/&gt; that</rdg>
		</rdgGrp>
		<rdgGrp
			n="['i', 'was', 'lost', 'in', 'conjecture', 'as', 'to', 'the', 'cause', 'of', 'this;', 'but', 'yesterday', 'an', 'idea', 'struck', 'me,', 'and', 'if', 'it', 'is', 'well', 'founded,']">
			<rdg wit="f1818">I was lost in conjecture as to the cause of this; but yesterday an idea
				struck me, and if it is well founded,</rdg>
			<rdg wit="f1823">I was lost in conjecture as to the cause of this; but yesterday an idea
				struck me, and if it is well founded,</rdg>
			<rdg wit="fThomas">I was lost in conjecture as to the cause of this; but yesterday an
				idea struck me, and if it is well founded,</rdg>
			<rdg wit="f1831">I was lost in conjecture as to the cause of this; but yesterday an idea
				struck me, and if it is well founded,</rdg>
		</rdgGrp>
	</app>
```
- [x] **Confusion:** Are these supposed to be in the same app? the MS has very little in common with everything else.

```
<app>
		<rdgGrp
			n="['female', 'without', '&lt;delstart/&gt;fresh&lt;delend/&gt;', 'again', 'devoting', '', '', 'several', '', 'months', 'to', 'study']">
			<rdg wit="fMS">female without &lt;del rend="strikethrough"
				xml:id="c57-0075__main__d4e14744"&gt;fresh&lt;/del&gt; again devoting &lt;mod
				sID="c57-0075__main__d4e14747"/&gt;&lt;sga-add place="sublinear"
				sID="c57-0075__main__d4e14749"/&gt; &lt;metamark
				function="insert"&gt;^&lt;/metamark&gt; &lt;sga-add
				eID="c57-0075__main__d4e14749"/&gt;&lt;sga-add place="superlinear"
				sID="c57-0075__main__d4e14755"/&gt;several &lt;sga-add
				eID="c57-0075__main__d4e14755"/&gt;&lt;mod eID="c57-0075__main__d4e14747"/&gt;
				months &lt;lb n="c57-0075__main__4"/&gt;to study</rdg>
		</rdgGrp>
		<rdgGrp
			n="['point', 'would', 'be', 'not', 'only', 'useless,', 'but', 'draw', 'down', 'treble', 'misery', 'on', 'us', 'all.&#34;', '&lt;p-end/&gt;', '&lt;p-start/&gt;', 'i', 'trembled', 'violently', 'at']">
			<rdg wit="f1818">point would be not only &lt;pb xml:id="F1818_v3_008"
				n="004"/&gt;useless, but draw down treble misery on us all.” &lt;p
				eID="novel1_letter4_chapter17_div4_div19_p3"/&gt; &lt;p
				sID="novel1_letter4_chapter17_div4_div19_p4"/&gt; I trembled violently at</rdg>
			<rdg wit="f1823">point would be not only use&lt;pb xml:id="F1823_v2_365"
				n="92"/&gt;less, but draw down treble misery on us all.” &lt;p
				eID="novel1_letter4_chapter17_div4_div18_p3"/&gt; &lt;p
				sID="novel1_letter4_chapter17_div4_div18_p4"/&gt; I trembled violently at</rdg>
			<rdg wit="fThomas">point would be not only &lt;pb xml:id="F1818_v3_008"
				n="004"/&gt;useless, but draw down treble misery on us all.” &lt;p
				eID="novel1_letter4_chapter17_div4_div19_p3"/&gt; &lt;p
				sID="novel1_letter4_chapter17_div4_div19_p4"/&gt; I trembled violently at</rdg>
			<rdg wit="f1831">point would be not only useless, but draw down treble misery on us
				all.” &lt;p eID="novel1_letter4_chapter18_div4_div18_p3"/&gt; &lt;p
				sID="novel1_letter4_chapter18_div4_div18_p4"/&gt; I trembled violently at</rdg>
		</rdgGrp>
	</app>
```

- Ending Point: "Laborious Disquisition"
    * This section appears to have a lot of misalignments that prevent me from getting very far at the start. Let's fix these so we can move forward in a timely fashion.
    
- Testing to see if my new branch is working properly

# 4-18-2023

- [ ] **MS Snag:** "My Health" may not align properly in the MS compared to other versions
** Dr. B to fix this manually: the MS witness has the phrase, "my health ... which had hitherto declined" as a second token AFTEr the long token we placed re composing a female.**
- [ ] **Fix Manually:** MS "My Health"
```
<app>
		<rdgGrp n="['my']">
			<rdg wit="f1818">my</rdg>
			<rdg wit="f1823">my</rdg>
			<rdg wit="fThomas">my</rdg>
			<rdg wit="fMS">&lt;lb n="c57-0074__main__7"/&gt;My</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['health', '&lt;del&gt;also&lt;/del&gt;']">
			<rdg wit="fMS">health &lt;del rend="strikethrough"
				xml:id="c57-0074__main__d4e14518"&gt;also&lt;/del&gt;</rdg>
		</rdgGrp>
		<rdgGrp n="['returning', 'tranquillity.']">
			<rdg wit="f1818">returning tranquillity.</rdg>
			<rdg wit="f1823">returning tranquillity.</rdg>
			<rdg wit="fThomas">returning tranquillity.</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['my', 'health,']">
			<rdg wit="f1818">My health,</rdg>
			<rdg wit="f1823">My health,</rdg>
			<rdg wit="fThomas">My health,</rdg>
			<rdg wit="f1831">my health,</rdg>
```
- [x] **Confusion:** "Compose a female" shows up significantly later in the MS while the other passages go on about something else, yet the alignment seems normal. Needs inspection, could be another snag.

-  **Observation:** The MS seems very different, hardly mentioning the topic of marriage and disappearing for several apps. It's as if the entire MS is snagged.

- ebb: We repaired with longTokens: the MS was repeating this passage. 

# 4-19-2023


- [x] MS "For some time"
 **Finishing Point:** "Those Philosophers"

# 4-26-2023
- Haven't had a lot of time to work on this branch lately, I've had to work on final projects instead.
- Reran collation for C24. Some changes appear to have been made, but I don't know if any problems were solved.
- [x] **Possible Snag:** 1831 has this passage below spread across several apps, but in the colation, I don't know if it's aligned properly. 

```
I had an insurmountable aversion to the idea of engaging myself in my loathsome
            task in my father’s house, while in habits of familiar intercourse with those I loved. I
            knew that a thousand fearful accidents might occur,
```
- [x] There is a lot of divergence in 1831 starting in the aforementioned passage, but I don't know if all of it is aligned properly. It could just be that 1831 is written differently.
- [x] **Possible misalignment:** Why is absence in 1831 in the app before all the others? Needs inspection
```
<app>
		<rdgGrp n="['my', 'unearthly', 'occupation.', 'i', 'must', 'absent', 'myself']">
			<rdg wit="f1831">my unearthly occupation. I must absent myself</rdg>
		</rdgGrp>
		<rdgGrp n="['occupation']">
			<rdg wit="fMS">occupation</rdg>
		</rdgGrp>
		<rdgGrp n="['occupation,']">
			<rdg wit="f1818">occupation,</rdg>
			<rdg wit="f1823">occupation,</rdg>
			<rdg wit="fThomas">occupation,</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['in', 'absence']">
			<rdg wit="f1818">in absence</rdg>
			<rdg wit="f1823">in absence</rdg>
			<rdg wit="fThomas">in absence</rdg>
			<rdg wit="fMS">in absence</rdg>
		</rdgGrp>
	</app>
```
- [x] **Confusion:** Should this passage be aligned differently for 1831? It doesn't seem right.
```
app>
		<rdgGrp n="['have']">
			<rdg wit="f1818">have</rdg>
			<rdg wit="f1823">have</rdg>
			<rdg wit="fThomas">have</rdg>
			<rdg wit="fMS">&lt;lb n="c57-0082__main__15"/&gt;have</rdg>
		</rdgGrp>
		<rdgGrp n="['would', 'depart', 'for', 'ever.']">
			<rdg wit="f1831">would depart for ever.</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['departed']">
			<rdg wit="fMS">departed</rdg>
		</rdgGrp>
		<rdgGrp n="['departed;']">
			<rdg wit="f1818">departed;</rdg>
			<rdg wit="f1823">departed;</rdg>
			<rdg wit="fThomas">departed;</rdg>
		</rdgGrp>
	</app>
```
- **Morning Finishing point:** "Ending to my slavery forever"

# 4-30-2023
- [x] **Confusion:** These apps are aligned properly, but should "forever" be one word rather than two, or should I leave it as-is?
```
<app>
		<rdgGrp n="['end', 'to', 'my', 'slavery', 'for']">
			<rdg wit="f1818">end to my slavery for</rdg>
			<rdg wit="f1823">end to my slavery for</rdg>
			<rdg wit="fThomas">end to my slavery for</rdg>
			<rdg wit="f1831">end to my slavery for</rdg>
			<rdg wit="fMS">end to my &lt;lb n="c57-0082__main__17"/&gt;slavery for</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['ever.', '&lt;p-end/&gt;', '&lt;p-start/&gt;', 'these']">
			<rdg wit="f1818">ever. &lt;p eID="novel1_letter4_chapter17_div4_div19_p9"/&gt; &lt;p
				sID="novel1_letter4_chapter17_div4_div19_p10"/&gt; These</rdg>
			<rdg wit="f1823">ever. &lt;p eID="novel1_letter4_chapter17_div4_div18_p9"/&gt; &lt;p
				sID="novel1_letter4_chapter17_div4_div18_p10"/&gt; These</rdg>
			<rdg wit="fThomas">ever. &lt;p eID="novel1_letter4_chapter17_div4_div19_p9"/&gt; &lt;p
				sID="novel1_letter4_chapter17_div4_div19_p10"/&gt; These</rdg>
			<rdg wit="f1831">ever. &lt;p eID="novel1_letter4_chapter18_div4_div18_p9"/&gt; &lt;p
				sID="novel1_letter4_chapter18_div4_div18_p10"/&gt; These</rdg>
		</rdgGrp>
		<rdgGrp n="['ever—these']">
			<rdg wit="fMS">ever—These</rdg>
		</rdgGrp>
	</app>
```
- [x] **Possible Misalignment Detected:** 1831 disappears after "guise," and the passages after it are very wordy. I'll post a code sample below, and when it does appear, it has almost nothing in common with the passages it's aligned with
```
<app>
		<rdgGrp n="['of']">
			<rdg wit="f1818">of</rdg>
			<rdg wit="f1823">of</rdg>
			<rdg wit="fThomas">of</rdg>
			<rdg wit="fMS">of</rdg>
		</rdgGrp>
		<rdgGrp
			n="['which', 'excited', 'no', 'suspicion,', 'while', 'i', 'urged', 'my', 'desire', 'with', 'an', 'earnestness', 'that', 'easily', 'induced', 'my', 'father', 'to', 'comply.', 'after', 'so', 'long', 'a', 'period', 'of']">
			<rdg wit="f1831">which excited no suspicion, while I urged my desire with an earnestness
				that easily induced my father to comply. After so long a period of</rdg>
		</rdgGrp>
	</app>

	<app>
		<rdgGrp n="['&lt;del&gt;wh&lt;/del&gt;']">
			<rdg wit="fMS">&lt;del instant="true" rend="strikethrough"
				xml:id="c57-0082__main__d4e15296"&gt;wh&lt;/del&gt;</rdg>
		</rdgGrp>
		<rdgGrp
			n="['an', 'absorbing', 'melancholy,', 'that', 'resembled', 'madness', 'in', 'its', 'intensity']">
			<rdg wit="f1831">an absorbing melancholy, that resembled madness in its intensity</rdg>
		</rdgGrp>
	</app>
```

- [x] **Another MS and 1831 group:** This one could have the MS be misaligned, as Elizabeth is mentioned a few apps prior in all the other scripts, including 1831!
```
<app>
		<rdgGrp
			n="['an', 'impediment,', 'and', 'truly', 'i', 'rejoiced', 'that', 'thus', 'i', 'should', 'be', 'saved', 'many', 'hours', 'of', 'lonely,', 'maddening', 'reflection.', 'nay,', 'henry', 'might', 'stand', 'between', 'me', 'and', 'the', 'intrusion', 'of', 'my', 'foe.', 'if']">
			<rdg wit="f1831">an impediment, and truly I rejoiced that thus I should be saved many
				hours of lonely, maddening reflection. Nay, Henry might stand between me and the
				intrusion of my foe. If</rdg>
		</rdgGrp>
		<rdgGrp n="['united', 'to', 'elizabeth']">
			<rdg wit="fMS">united to Elizabeth</rdg>
		</rdgGrp>
	</app>
```
- [x] **Confusion:** In the section below, the MS appears as a blank token. In the manuscript, there is a to there, but there is possibly an issue with the file that needs to be resolved so the word can be picked up.
```
<app>
		<rdgGrp n="['', '&lt;del&gt;to me que&lt;/del&gt;']">
			<rdg wit="fMS">&lt;lb n="c57-0085__main__2"/&gt; &lt;del rend="strikethrough"
				xml:id="c57-0085__main__d4e15491"&gt;to me que&lt;/del&gt;</rdg>
		</rdgGrp>
		<rdgGrp n="['to']">
			<rdg wit="f1818">to</rdg>
			<rdg wit="f1823">to</rdg>
			<rdg wit="fThomas">to</rdg>
		</rdgGrp>
	</app>
```

- **NOTE:** 1831 finally realigns with the other drafts starting with "I now made arrangements." I sense a MASSIVE longToken for 1831 in the future.
- **Finishing Point:** "Danger of his machinations."

# 5-4-2023

- [x] **To be fixed:** MS "I passed through" needs to be aligned to all the other witnesses

- **NOTE:** Wrapping `<del rend="strikethrough" xml:id="c57-0086__main__d4e15665">possibility of</del> danger  <sga-add hand="#pbs" place="superlinear" sID="c57-0086__main__d4e15668"/>of his machinations <sga-add eID="c57-0086__main__d4e15668"/>. <delSpan rend="strikethrough" spanTo="#c57-0086.01"/>Thinking
        thus <lb n="c57-0086__main__6"/>I prepared for my journey` 

  and

   `I passed th  <mod sID="c57-0087__main__d4e15690"/> <sga-add place="sublinear" sID="c57-0087__main__d4e15692"/> <metamark function="insert">^</metamark> <sga-add eID="c57-0087__main__d4e15692"/> <sga-add place="superlinear" sID="c57-0087__main__d4e15698"/>r <sga-add eID="c57-0087__main__d4e15698"/> <mod eID="c57-0087__main__d4e15690"/> ough` 

  with longToken in MS.

# 6-5-2023
- [X] **Merge:** The second app should be merge into the first app.
```xml
<app>
    <rdgGrp n="['ocean,']">
        <rdg wit="f1818">ocean,</rdg>
        <rdg wit="f1823">ocean,</rdg>
        <rdg wit="fThomas">ocean,</rdg>
    </rdgGrp>
    <rdgGrp n="['ocean;']">
        <rdg wit="f1831">ocean;</rdg>
    </rdgGrp>
    <rdgGrp n="['ocean–and']">
        <rdg wit="fMS">ocean–and</rdg>
    </rdgGrp>
</app>
<app>
    <rdgGrp n="['and']">
        <rdg wit="f1818">and</rdg>
        <rdg wit="f1823">and</rdg>
        <rdg wit="fThomas">and</rdg>
        <rdg wit="f1831">and</rdg>
    </rdgGrp>
</app>
```
- **Note:** wrapping `ocean; and` with longToken in 1831.

- [x] **Merge:** The second app should be merged to the first one.

```xml
  
<app>
    <rdgGrp n="['for']">
        <rdg wit="f1823">for</rdg>
        <rdg wit="f1831">for</rdg>
    </rdgGrp>
    <rdgGrp n="['forever?']">
        <rdg wit="f1818">forever?</rdg>
        <rdg wit="fThomas">forever?</rdg>
    </rdgGrp>
</app>
<app>
    <rdgGrp n="['ever', '?']">
        <rdg wit="f1823">ever ?</rdg>
    </rdgGrp>
    <rdgGrp n="['ever?']">
        <rdg wit="f1831">ever?</rdg>
    </rdgGrp>
</app>
```

- **Note:** Wrapping longToken around `for ever?` in 1831
- [x] 2023-07-09 ebb: correct fused token: `scene&` around change of scene passage
- [x] 2023-07-09 ebb: extend a longToken to unite the MS w/ other witnesses around this passage:
     "that the fiend would follow me and exempt me/my family from the danger of his machinations."  

- [x] **Misalignment:** In MS, two sentences are different from three paragraphs in other editions. The longToken doesn't work because the algorithm can't identify where they should come together correctly. They should go back together at `cologne we descended`. (Search `cologne we descended` in `Collation_C24-complete-june5.xml` to see how MS is far from other editions.) 

  Thus, I try to wrap longToken around the two sentences in MS and the last two paragraphs of the three paragraphs. However, the two paragraphs are a little bit lengthy. A better solution to address this misalignment is expected.
  2023-07-09 ebb: I'm solving this by moving the "Cologne" passage through the end of C24 over to the start of C25, to force the sections to align properly. 