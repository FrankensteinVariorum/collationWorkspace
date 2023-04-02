# 3-25-2023

- Establishing the branch, the complete files, and the readme. Running shell script here for the first time.
- [X] MS: `have` is written as `ha ve`. Can't remember if `<sga>` code prevents this from being fixable or not.
- [X] **Confusion::** MS has `in`, but every other version has `that had broken`. Those two statements align, and the next passages appear to be aligned. See below for reference:
```<app>
		<rdgGrp n="['in']">
			<rdg wit="fMS">in</rdg>
		</rdgGrp>
		<rdgGrp n="['that', 'had', 'broken']">
			<rdg wit="f1818">that had broken</rdg>
			<rdg wit="f1823">that had broken</rdg>
			<rdg wit="fThomas">that had broken</rdg>
			<rdg wit="f1831">that had broken</rdg>
		</rdgGrp>
	</app>
```	

- [X] **Possible misalignment:** one app has `arch` and `arch-fiend,` in the same reading group, but everything except 1831 has `arch` and `fiend` in separate apps. May need to fix with longTokens, see code below for reference:
```
<app>
		<rdgGrp n="['arch']">
			<rdg wit="f1818">arch</rdg>
			<rdg wit="f1823">arch</rdg>
			<rdg wit="fThomas">arch</rdg>
			<rdg wit="fMS">&lt;sga-add place="superlinear"
				sID="c57-0051__main__d4e10089"/&gt;arch</rdg>
		</rdgGrp>
		<rdgGrp n="['arch-fiend,']">
			<rdg wit="f1831">arch-fiend,</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['', 'fiend']">
			<rdg wit="fMS">&lt;sga-add eID="c57-0051__main__d4e10089"/&gt; fiend</rdg>
		</rdgGrp>
		<rdgGrp n="['fiend,']">
			<rdg wit="f1818">fiend,</rdg>
			<rdg wit="f1823">fiend,</rdg>
			<rdg wit="fThomas">fiend,</rdg>
		</rdgGrp>
	</app>
```	
- Finishing Point: "Arch-Fiend"

# 3-28-2023
- [X] **Misalignment Detected:** "To have familiarized" in the MS has the entire phrase grouped with `to have`, but `familiarized` is not grouped with the other four sections. `longToken` may be necessary for isolation.:
```
<app>
		<rdgGrp n="['to', 'have']">
			<rdg wit="f1818">to have</rdg>
			<rdg wit="f1823">to have</rdg>
			<rdg wit="fThomas">to have</rdg>
			<rdg wit="f1831">to have</rdg>
		</rdgGrp>
		<rdgGrp n="['tohave', 'familia', '&lt;delstart/&gt;rzi&lt;delend/&gt;', 'r', '', 'ized']">
			<rdg wit="fMS">to&lt;lb n="c57-0053__main__1"/&gt;have familia &lt;del
				rend="overwritten" xml:id="c57-0053__main__d4e10385"&gt;rzi&lt;/del&gt; &lt;sga-add
				place="intralinear" sID="c57-0053__main__d4e10388"/&gt;r &lt;sga-add
				eID="c57-0053__main__d4e10388"/&gt; ized</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['familiarised']">
			<rdg wit="f1831">familiarised</rdg>
		</rdgGrp>
		<rdgGrp n="['familiarized']">
			<rdg wit="f1818">familiarized</rdg>
			<rdg wit="f1823">familiarized</rdg>
			<rdg wit="fThomas">familiarized</rdg>
		</rdgGrp>
	</app>
```	

- Finishing Point: "We can never again inhabit that cottage"

# 3-29-2023
- [X] Alignment error: garden misaligned in MS, being split up with the word "the" Find with "vestige of cultivation"
- - Finishing Point: "and bitterness"

# 4-2-2023
- **Confusion:** What's up with the manuscript here?

```
<app>
		<rdgGrp
			n="['', '', 'me', '', '&lt;p-end/&gt;', '&lt;p-start/&gt;', 'as', 'i', 'continued', 'my', 'way', 'in', 'this', 'mood', 'i', 'heard', 'a', 'voices', 'which', 'forced', 'me', 'to', 'conceal', 'myself.', 'this', 'i', 'did', 'in', 'a', 'small', 'cave', 'surrounded', 'by', 'wood', 'at', 'the', 'foot', 'of', 'which', 'was', 'a', '', '&lt;mdel&gt;', '&lt;/mdel&gt;', '', '', 'deep', 'and', 'impetuous', '', 'river', '–', 'i', 'presently', 'discovered', 'that', 'the', 'voices', 'proceeded', 'from', 'people', 'who', 'were', 'on', 'the', 'rock', 'which', 'formed', 'the', 'roof', 'of', 'the', 'cavern', '–', 'they', 'spoke', 'a', 'language', 'unknown', 'to', 'me', '–', 'when', 'suddenly', 'i', 'heard', 'a', 'noise', 'and', 'saw', 'a', '&lt;delstart/&gt;woma&lt;delend/&gt;', 'young', 'girl', 'fall', 'from', 'the', 'precipiece', 'into', 'the', 'river', 'a', '', '&lt;delstart/&gt;and aloud&lt;delend/&gt;', 'loud', 'scream', 'followed', 'and', 'all', 'was', 'quiet–', 'i', 'rushed', 'from', 'my', 'hiding', 'place', 'and', 'dashing', 'into', 'the', 'river', 'rescued', 'the', 'girl', 'and', 'bore', 'her', 'to', 'the', 'shore.', 'she', 'was', 'senseless', 'and', 'i', 'endeavoured', 'to', 'restore', 'her', 'to', 'life', 'when', 'a', 'man', 'came', 'suddenly', 'from', 'the', 'woods', 'and', 'appeared', 'aghas', '']">
			<rdg wit="fMS">&lt;mod sID="c57-0059__main__d4e11784"/&gt;&lt;sga-add place="sublinear"
				sID="c57-0059__main__d4e11786"/&gt; &lt;metamark
				function="insert"&gt;^&lt;/metamark&gt; &lt;sga-add
				eID="c57-0059__main__d4e11786"/&gt;&lt;sga-add place="superlinear"
				sID="c57-0059__main__d4e11792"/&gt;me &lt;sga-add
				eID="c57-0059__main__d4e11792"/&gt;&lt;mod eID="c57-0059__main__d4e11784"/&gt;
				&lt;milestone unit="tei:p-END"/&gt; &lt;milestone unit="tei:p-START"/&gt;
				&lt;delSpan rend="vertical_line" spanTo="#c57-0060.01"/&gt;&lt;lb
				n="c57-0060__main__1"/&gt;As I continued my way in this mood I &lt;lb
				n="c57-0060__main__2"/&gt;heard a voices which forced me to conceal &lt;w
				ana="start"/&gt;my&lt;lb n="c57-0060__main__3"/&gt;self&lt;w ana="end"/&gt;. This I
				did in a small cave surrounded by &lt;lb n="c57-0060__main__4"/&gt;wood at the foot
				of which was a &lt;mod sID="c57-0060__main__d4e11821"/&gt; &lt;mdel&gt;
				&lt;/mdel&gt; &lt;sga-add place="sublinear" sID="c57-0060__main__d4e11828"/&gt;
				&lt;metamark function="insert"&gt;^&lt;/metamark&gt; &lt;sga-add
				eID="c57-0060__main__d4e11828"/&gt;&lt;sga-add place="superlinear"
				sID="c57-0060__main__d4e11834"/&gt;deep &amp; impetuous &lt;sga-add
				eID="c57-0060__main__d4e11834"/&gt;&lt;mod eID="c57-0060__main__d4e11821"/&gt; river
				– I &lt;lb n="c57-0060__main__5"/&gt;presently discovered that the voices proceeded
				&lt;lb n="c57-0060__main__6"/&gt;from people who were on the rock which &lt;lb
				n="c57-0060__main__7"/&gt;formed the roof of the cavern – They spoke a &lt;lb
				n="c57-0060__main__8"/&gt;language unknown to me – when suddenly &lt;lb
				n="c57-0060__main__9"/&gt;I heard a noise and saw a &lt;del instant="true"
				rend="strikethrough" xml:id="c57-0060__main__d4e11849"&gt;woma&lt;/del&gt; young
				girl &lt;lb n="c57-0060__main__10"/&gt;fall from the precipiece into the river a
				&lt;lb n="c57-0060__main__11"/&gt; &lt;del instant="true" rend="strikethrough"
				xml:id="c57-0060__main__d4e11857"&gt;and aloud&lt;/del&gt; loud scream followed
				&amp; all was quiet– &lt;lb n="c57-0060__main__12"/&gt;I rushed from my hiding place
				&amp; dashing into &lt;lb n="c57-0060__main__13"/&gt;the river rescued the girl
				&amp; bore her to the &lt;lb n="c57-0060__main__14"/&gt;shore. She was senseless
				&amp; I endeavoured to &lt;lb n="c57-0060__main__15"/&gt;restore her to life when a
				man came &lt;w ana="start"/&gt;sudden&lt;lb n="c57-0060__main__16"/&gt;ly&lt;w
				ana="end"/&gt; from the woods and appeared aghas &lt;anchor
				xml:id="c57-0060.01"/&gt;</rdg>
		</rdgGrp>
		<rdgGrp n="['me.']">
			<rdg wit="f1818">me.</rdg>
			<rdg wit="f1823">me.</rdg>
			<rdg wit="fThomas">me.</rdg>
			<rdg wit="f1831">me.</rdg>
		</rdgGrp>
	</app>
```	

- [] **Possible Misalignment Detected:** `Cypress` is differently aligned in the MS, but I can't say for sure. Needs evaluation.

```
<app>
		<rdgGrp n="['a']">
			<rdg wit="f1818">a</rdg>
			<rdg wit="f1823">a</rdg>
			<rdg wit="fThomas">a</rdg>
			<rdg wit="f1831">a</rdg>
		</rdgGrp>
		<rdgGrp
			n="['cypress.', 'a', 'rustic', 'approached', 'armed', 'with', 'a', 'gun', 'and', 'leading', 'a']">
			<rdg wit="fMS">cypress. &lt;delSpan rend="strikethrough" spanTo="#c57-0060.02"/&gt;A
				rustic approached armed &lt;lb n="c57-0060__main__25"/&gt;with a gun and leading
				a</rdg>
		</rdgGrp>
	</app>

	<app>
		<rdgGrp n="['cypress.']">
			<rdg wit="f1818">cypress.</rdg>
			<rdg wit="f1823">cypress.</rdg>
			<rdg wit="fThomas">cypress.</rdg>
			<rdg wit="f1831">cypress.</rdg>
		</rdgGrp>
		<rdgGrp
			n="['young', 'girl', 'of', 'about', 'twelve', 'years', 'of', 'age', 'when', 'they', 'came', 'near', 'me', 'they', 'turne']">
			<rdg wit="fMS">young girl of about twelve &lt;lb n="c57-0060__main__26"/&gt;years of age
				When they came near me they turne</rdg>
		</rdgGrp>
	</app>
```	
- [] **Misalignment Detected:** `Hiding Place` is different in some readings of the story, and much like `arch-fiend,` It's separated into reading groups because of word separation. May need a similar fix, code is listed below:
```
<app>
		<rdgGrp n="['hiding']">
			<rdg wit="f1818">hiding</rdg>
			<rdg wit="fThomas">hiding</rdg>
			<rdg wit="fMS">hiding</rdg>
		</rdgGrp>
		<rdgGrp n="['hiding-place,']">
			<rdg wit="f1823">hiding-place,</rdg>
		</rdgGrp>
		<rdgGrp n="['hiding-place;']">
			<rdg wit="f1831">hiding-place;</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['place', 'and']">
			<rdg wit="fMS">&lt;lb n="c57-0060__main__33"/&gt;place and</rdg>
		</rdgGrp>
		<rdgGrp n="['place,']">
			<rdg wit="f1818">place,</rdg>
			<rdg wit="fThomas">place,</rdg>
		</rdgGrp>
	</app>
```
- [] **Side Note:** This also causes `and` to be misaligned in the MS, that word should be moved down. See below:
```
<app>
		<rdgGrp n="['and,']">
			<rdg wit="f1818">and,</rdg>
			<rdg wit="f1823">and,</rdg>
			<rdg wit="fThomas">and,</rdg>
			<rdg wit="f1831">and,</rdg>
		</rdgGrp>
	</app>
```	
- **Confusion:** Some passages have `This then was`while others have '`This was then` in three separate apps. Because of how similar the wording is, should they be combined into one app? Code listed below:

```
<app>
		<rdgGrp n="['&#34;this']">
			<rdg wit="f1818">“This</rdg>
			<rdg wit="f1823">“This</rdg>
			<rdg wit="fThomas">“This</rdg>
			<rdg wit="f1831">“This</rdg>
		</rdgGrp>
		<rdgGrp n="['this', 'then']">
			<rdg wit="fMS">&lt;lb n="c57-0061__main__14"/&gt;This then</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['was']">
			<rdg wit="f1818">was</rdg>
			<rdg wit="f1823">was</rdg>
			<rdg wit="fThomas">was</rdg>
			<rdg wit="f1831">was</rdg>
			<rdg wit="fMS">was</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['then']">
			<rdg wit="f1818">then</rdg>
			<rdg wit="f1823">then</rdg>
			<rdg wit="fThomas">then</rdg>
			<rdg wit="f1831">then</rdg>
		</rdgGrp>
	</app>
```

- **Finishing point:** "The reward of my benevolence"