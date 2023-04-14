# 4-12-2023
- Establishing branch and running collation for the first time

# 4-14-2023

-[X] **Confusion** In the first `<app>`, the Chapter for the MS is listed. Shouldn't it be in the second app? 

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
-[] **Confusion:** For "I was unable to overcome my repugnance", I found a similar phrase in the MS, yet it was not detected by the script. It may have been a deletion, needs evaluation.

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

-[] **Misalignment Detected:** The manuscript's phrase of "I was unable to overcome my repugnance" comes later than every other edition, possibly due to word order in the drafts. The MS disappears at several points (indicating that the MS did not contain certain passages), but there is a lot of overlap where it shouldn't be, more than I can copy and paste.

-[] **Confusion:** MS has the phrase "alone in a little boat" appear about two apps sooner than when it appears in other editions, yet the passage before it appears well aligned. I'll post the cope snippets, but something isn't right.

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

-[] **Confusion:** What's going on here?

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
-[] **Confusion:** Are these supposed to be in the same app? the MS has very little in common with everything else.

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