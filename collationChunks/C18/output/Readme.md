# 2-15-2023

- [X] Fixed "Suffered from" fixed the MS, where there was a space between "fro" and "m"

- [X] MS: added a space for "motive of"

- Finishing point: "day was passed in the same routine"

# 2-17-2023

- [ ] MS mentions departing on a mammal rather than a first meal. It's in a different reading group, but in the same app as the meals. It's mainly sligned with the meal statements because they all end with the same word: **This**
- [ ] All versions: does a new chapter start after "benevolent smiles?" Should I add a token? The code confuses me, should I change anything in this code block?

```
<app>
		<rdgGrp n="['&lt;p-end/&gt;', '&lt;p-start/&gt;']">
			<rdg wit="f1818">&lt;p eID="novel1_letter4_chapter11_div4_div12_p3"/&gt; &lt;p
				sID="novel1_letter4_chapter11_div4_div12_p4"/&gt;</rdg>
			<rdg wit="f1823">&lt;p eID="novel1_letter4_chapter11_div4_div11_p3"/&gt; &lt;p
				sID="novel1_letter4_chapter11_div4_div11_p4"/&gt;</rdg>
			<rdg wit="fThomas">&lt;p eID="novel1_letter4_chapter11_div4_div12_p3"/&gt; &lt;p
				sID="novel1_letter4_chapter11_div4_div12_p4"/&gt;</rdg>
			<rdg wit="f1831">&lt;p eID="novel1_letter4_chapter12_div4_div12_p3"/&gt; &lt;p
				sID="novel1_letter4_chapter12_div4_div12_p4"/&gt;</rdg>
		</rdgGrp>
		<rdgGrp n="['&lt;delstart/&gt;b&lt;delend/&gt;', '&lt;p-end/&gt;', '&lt;p-start/&gt;']">
			<rdg wit="fMS">&lt;del rend="strikethrough"
				xml:id="c57-0016__main__d4e3343"&gt;B&lt;/del&gt; &lt;milestone
				unit="tei:p-END"/&gt; &lt;milestone unit="tei:p-START"/&gt;</rdg>
		</rdgGrp>
	</app>
```	
- [ ] MS: "Company and speech has "and speech and" in the same reading group, whereas every other iteration has "and" in an individual group, with "speech, interchanging" in a separate reading group. The manuscript's phrase is "and speech and interchanged." Debating adding a longToken and/or adjusting the spacing. Code samples listed below:

```
<rdgGrp n="['and']">
			<rdg wit="f1818">and</rdg>
			<rdg wit="f1823">and</rdg>
			<rdg wit="fThomas">and</rdg>
			<rdg wit="f1831">and</rdg>
		</rdgGrp>
		<rdgGrp n="['and', 'speech', '', '—', 'and']">
			<rdg wit="fMS">&lt;sga-add place="superlinear" sID="c57-0017__main__d4e3460"/&gt;&amp;
				speech &lt;sga-add eID="c57-0017__main__d4e3460"/&gt; — and</rdg>
		</rdgGrp>
	</app>
```	

```
<app>
		<rdgGrp n="['&lt;delstart/&gt;saw&lt;delend/&gt;', 'interchanged']">
			<rdg wit="fMS">&lt;del rend="strikethrough"
				xml:id="c57-0017__main__d4e3464"&gt;saw&lt;/del&gt; &lt;lb
				n="c57-0017__main__10"/&gt;&lt;lb n="c57-0017__left_margin__1"/&gt;&lt;sga-add
				sID="c57-0017__left_margin__d4e3475"/&gt;interchanged</rdg>
		</rdgGrp>
		<rdgGrp n="['speech,', 'interchanging']">
			<rdg wit="f1818">speech, interchanging</rdg>
			<rdg wit="f1823">speech, interchanging</rdg>
			<rdg wit="fThomas">speech, interchanging</rdg>
			<rdg wit="f1831">speech, interchanging</rdg>
		</rdgGrp>
	</app>
```
- [ ] MS: "seemed at first enigmatic" seemed is missing, not in the same app as "were," not detected at all by shellScript. Debating what to do here.
- [ ] **Added Note:** seemed appears to be in a different reading group, with enigmatic and the chapter header entwined into it. Other versions only have entwined and the chpater header intertwined. Seemed is definitely in the wrong place, though.

```
<rdgGrp n="['enigmatic.', '&lt;p-end/&gt;', '&lt;p-start/&gt;', '&#34;a']">
			<rdg wit="f1818">enigmatic. &lt;p eID="novel1_letter4_chapter11_div4_div12_p4"/&gt;
				&lt;p sID="novel1_letter4_chapter11_div4_div12_p5"/&gt; &lt;pb xml:id="F1818_v2_060"
				n="056"/&gt;“A</rdg>
			<rdg wit="f1823">enigmatic. &lt;p eID="novel1_letter4_chapter11_div4_div11_p4"/&gt;
				&lt;p sID="novel1_letter4_chapter11_div4_div11_p5"/&gt; &lt;pb xml:id="F1823_v1_256"
				n="237"/&gt;“A</rdg>
			<rdg wit="fThomas">enigmatic. &lt;p eID="novel1_letter4_chapter11_div4_div12_p4"/&gt;
				&lt;p sID="novel1_letter4_chapter11_div4_div12_p5"/&gt; &lt;pb xml:id="F1818_v2_060"
				n="056"/&gt;“A</rdg>
			<rdg wit="f1831">enigmatic. &lt;p eID="novel1_letter4_chapter12_div4_div12_p4"/&gt;
				&lt;p sID="novel1_letter4_chapter12_div4_div12_p5"/&gt; “A</rdg>
		</rdgGrp>
		<rdgGrp
			n="['seemed', '', '&lt;delstart/&gt;igmmatic&lt;delend/&gt;', 'enigmatic', '', '.', '&lt;note_start/&gt;o you pretty pecksie!&lt;note_end/&gt;', '', '', 'chap. 3', '', '&lt;delstart/&gt;it was some time&lt;delend/&gt;', '', '', 'a']">
			<rdg wit="fMS">seemed &lt;lb n="c57-0017__main__17"/&gt; &lt;del rend="strikethrough"
				xml:id="c57-0017__main__d4e3495"&gt;igmmatic&lt;/del&gt; &lt;sga-add hand="#pbs"
				place="superlinear" sID="c57-0017__main__d4e3498"/&gt;enigmatic &lt;sga-add
				eID="c57-0017__main__d4e3498"/&gt; . &lt;note resp="#pbs"&gt;o you pretty
				Pecksie!&lt;/note&gt; &lt;lb n="c57-0018__main__1"/&gt; &lt;milestone
				spanTo="#c57-0018.05" unit="tei:head"/&gt; &lt;longToken&gt;Chap.
				3&lt;/longToken&gt; &lt;lb n="c57-0018__main__2"/&gt; &lt;del rend="strikethrough"
				xml:id="c57-0018__main__d4e3523"&gt;It was some time&lt;/del&gt; &lt;sga-add
				place="sublinear" sID="c57-0018__main__d4e3526"/&gt; &lt;metamark
				function="insert"&gt;^&lt;/metamark&gt; &lt;sga-add
				eID="c57-0018__main__d4e3526"/&gt;&lt;sga-add place="superlinear"
				sID="c57-0018__main__d4e3532"/&gt;A</rdg>
		</rdgGrp>
```

- [ ] Thomas: Possible Divergence detected! Similarities end after degree, and degree is isolate from its respective reading group. It's aligned again when discussing nourishment, however.

```
<rdgGrp
			n="['&lt;delstart/&gt;and they suffered that evil in a very distressing degree.&lt;delend/&gt;', '&lt;addedthomas-start/&gt;they had appeared to me rich, because their possessions incomparably transcended mine, but i soon learnt, that many of these advantages were only &lt;delstart/&gt;p&lt;/del-inner&gt; apparent, since their delicate frame made them subject to a thousand wants of the existence ofwhich i was entirely ignorant.&lt;addedthomas-end/&gt;']">
			<rdg wit="fThomas">&lt;del rend="strikethrough"&gt;and they suffered that evil in a very
				distressing degree.&lt;/del&gt; &lt;add place="bottom_and_prev_page_bottom"&gt;They
				had appeared to me rich, because their possessions incomparably transcended mine,
				but I soon learnt, that many of these advantages were only
				&lt;del-INNER&gt;p&lt;/del-INNER&gt; apparent, since their delicate frame made them
				subject to a thousand wants of the existence of &lt;pb n="56"/&gt; which I was
				entirely ignorant.&lt;/add&gt;</rdg>
		</rdgGrp>
```

- [ ] This section of code is confusing me. The group below it has "I" listed for everything but the manuscript, but why is this big code block here? 

```
<rdgGrp n="['', 'i', '&lt;delstart/&gt;found&lt;delend/&gt;', '', '']">
			<rdg wit="fMS">&lt;sga-add eID="c57-0018__main__d4e3742"/&gt; I &lt;del
				rend="strikethrough" xml:id="c57-0018__main__d4e3748"&gt;found&lt;/del&gt;
				&lt;sga-add place="sublinear" sID="c57-0018__main__d4e3751"/&gt; &lt;metamark
				function="insert"&gt;^&lt;/metamark&gt;</rdg>
		</rdgGrp>
		<rdgGrp
			n="['&lt;note_start/&gt;thomas copy: pencil mark joins paragraphs.&lt;note_end/&gt;']">
			<rdg wit="fThomas">&lt;note resp="#ebb"&gt;Thomas copy: pencil mark joins
				paragraphs.&lt;/note&gt;</rdg>
		</rdgGrp>
		<rdgGrp n="['&lt;p-end/&gt;', '&lt;p-start/&gt;']">
			<rdg wit="f1818">&lt;p eID="novel1_letter4_chapter11_div4_div12_p6"/&gt; &lt;p
				sID="novel1_letter4_chapter11_div4_div12_p7"/&gt;</rdg>
			<rdg wit="f1823">&lt;p eID="novel1_letter4_chapter11_div4_div11_p6"/&gt; &lt;p
				sID="novel1_letter4_chapter11_div4_div11_p7"/&gt;</rdg>
			<rdg wit="f1831">&lt;p eID="novel1_letter4_chapter12_div4_div12_p6"/&gt; &lt;p
				sID="novel1_letter4_chapter12_div4_div12_p7"/&gt;</rdg>
		</rdgGrp>
```	

- Stopping point: "That he did not go to the forest that day"

# 2-22-2023

- [ ] MS: "Feelings to" includes the words grouped together, where every other edition has them grouped separately
- [ ] 1823 and 1831 are in separate apps rather than reading groups for the word "sometimes." Code listed below, could be a concern:

```
<app>
		<rdgGrp n="['', '']">
			<rdg wit="fMS">&lt;sga-add place="sublinear" sID="c57-0019__main__d4e4024"/&gt;
				&lt;metamark function="insert"&gt;^&lt;/metamark&gt;</rdg>
		</rdgGrp>
		<rdgGrp n="['sometimes,']">
			<rdg wit="f1823">sometimes,</rdg>
			<rdg wit="f1831">sometimes,</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['sometimes']">
			<rdg wit="f1818">sometimes</rdg>
			<rdg wit="fThomas">sometimes</rdg>
			<rdg wit="fMS">&lt;sga-add eID="c57-0019__main__d4e4024"/&gt;&lt;sga-add
				place="superlinear" sID="c57-0019__main__d4e4030"/&gt;sometimes</rdg>
		</rdgGrp>
	</app>
```	