# Chunk 29 Notes
## pass 1
- [X] transdisposition found
    ```
	<app>
		<rdgGrp n="['much']">
			<rdg wit="f1818">much</rdg>
			<rdg wit="f1823">much</rdg>
			<rdg wit="fThomas">much</rdg>
			<rdg wit="f1831">much</rdg>
			<rdg wit="fMS">much</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['you']">
			<rdg wit="f1818">you</rdg>
			<rdg wit="f1823">you</rdg>
			<rdg wit="fThomas">you</rdg>
			<rdg wit="f1831">you</rdg>
		</rdgGrp>
		<rdgGrp n="['must', 'you']">
			<rdg wit="fMS">must you</rdg>
		</rdgGrp>
	</app>

	<app>
		<rdgGrp n="['must']">
			<rdg wit="f1818">must</rdg>
			<rdg wit="f1823">must</rdg>
			<rdg wit="fThomas">must</rdg>
			<rdg wit="f1831">must</rdg>
		</rdgGrp>
	</app>
    ```
    - 2023-7-14: wrapped long token around "My poor cousin, how much you must have suffered!" in all versions
- [X] misalignment found
    ```
	<app>
		<rdgGrp n="['disturb', 'you']">
			<rdg wit="f1818">disturb you</rdg>
			<rdg wit="f1823">disturb you</rdg>
			<rdg wit="fThomas">disturb you</rdg>
			<rdg wit="f1831">disturb you</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['at', 'this']">
			<rdg wit="f1818">at this</rdg>
			<rdg wit="f1823">at this</rdg>
			<rdg wit="fThomas">at this</rdg>
			<rdg wit="f1831">at this</rdg>
			<rdg wit="fMS">at this</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['period', 'disturb', 'you']">
			<rdg wit="fMS">period disturb you</rdg>
		</rdgGrp>
		<rdgGrp n="['period,']">
			<rdg wit="f1818">period,</rdg>
			<rdg wit="f1823">period,</rdg>
			<rdg wit="fThomas">period,</rdg>
			<rdg wit="f1831">period,</rdg>
		</rdgGrp>
	</app>
    ```
    - 2023-7-14: wrapped longToken around "I would not disturb you at this period, when so many misfortunes weigh upon" in each version.
- [X] misalignment found
    ```
	<app>
		<rdgGrp n="['dis']">
			<rdg wit="fThomas">&lt;add place="gutter"&gt;dis&lt;/add&gt;</rdg>
		</rdgGrp>
		<rdgGrp n="['disinterested']">
			<rdg wit="f1831">disinterested</rdg>
		</rdgGrp>
		<rdgGrp n="['disinterrested']">
			<rdg wit="fMS">disinterrested</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['interested']">
			<rdg wit="f1818">interested</rdg>
			<rdg wit="f1823">interested</rdg>
			<rdg wit="fThomas">interested</rdg>
		</rdgGrp>
	</app>
    ```	
    - 2023-7-14: wrapped longToken around all variations of "so disinterrested"/"so interested"
        -  will just need to remove space before "so" in manuscript. otherwise, it works
- [X] misalignment found
    ```
	<app>
		<rdgGrp n="['time', '–', 'for']">
			<rdg wit="fMS">time – for</rdg>
		</rdgGrp>
		<rdgGrp n="['time;']">
			<rdg wit="f1818">time;</rdg>
			<rdg wit="fThomas">time;</rdg>
			<rdg wit="f1831">time;</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['for,']">
			<rdg wit="f1818">for,</rdg>
			<rdg wit="f1823">for,</rdg>
			<rdg wit="fThomas">for,</rdg>
			<rdg wit="f1831">for,</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['as', 'if', 'to']">
			<rdg wit="f1818">as if to</rdg>
			<rdg wit="f1823">as if to</rdg>
			<rdg wit="fThomas">as if to</rdg>
			<rdg wit="f1831">as if to</rdg>
			<rdg wit="fMS">as &lt;lb n="c57-0139__main__12"/&gt;if to</rdg>
		</rdgGrp>
    ```
    - 2023-7-14: wrapped longToken around all variations of "mean time; for,"
- [ ] misalignment found
    ```
	<app>
		<rdgGrp n="['&lt;del&gt;all&lt;/del&gt;']">
			<rdg wit="fMS">&lt;del rend="strikethrough" xml:id="c57-0139__main__d4e25924"&gt;all&lt;/del&gt;</rdg>
		</rdgGrp>
		<rdgGrp n="['centred in']">
			<rdg wit="f1823">&lt;longToken&gt;centred in&lt;/longToken&gt;</rdg>
			<rdg wit="f1831">&lt;longToken&gt;centred in&lt;/longToken&gt;</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['concentered in']">
			<rdg wit="f1818">&lt;longToken&gt;concentered in&lt;/longToken&gt;</rdg>
			<rdg wit="fThomas">&lt;longToken&gt;concentered in&lt;/longToken&gt;</rdg>
			<rdg wit="fMS">&lt;longToken&gt;concentered &lt;sga-add hand="#pbs" place="superlinear" sID="c57-0139__main__d4e25927"/&gt;in&lt;/longToken&gt;</rdg>
		</rdgGrp>
	</app>
    ```	
    - 2023-7-14: wrapped longToken around each variation of “little happiness remains for us on earth; yet". And, all variations of "concentered in"/"centred in"
        - The “little happiness remains" sentence is properly aligned. However, "concentered in"/"centred in" are still in the wrong nodes.
    - 2023-7-19: wrapped "concentered in you."/"centred in you."
- [X] weird section. In the book, it says "earnestly entreat", which is a little confusing. But it should be fine.
    ```
	<app>
		<rdgGrp n="['earnestly']">
			<rdg wit="f1818">earnestly</rdg>
			<rdg wit="f1823">earnestly</rdg>
			<rdg wit="fThomas">earnestly</rdg>
			<rdg wit="f1831">earnestly</rdg>
		</rdgGrp>
		<rdgGrp n="['&lt;del&gt;erne&lt;/del&gt;', 'earnestly']">
			<rdg wit="fMS">&lt;del instant="true" rend="strikethrough"
				xml:id="c57-0140__main__d4e25992"&gt;erne&lt;/del&gt; earnestly</rdg>
		</rdgGrp>
	</app>

	<app>
		<rdgGrp n="['entreat', 'of', 'youand i']">
			<rdg wit="fMS">entreat of you&amp;&lt;lb n="c57-0140__main__8"/&gt;I</rdg>
		</rdgGrp>
		<rdgGrp n="['entreat,', 'and', 'i']">
			<rdg wit="f1818">entreat, and I</rdg>
			<rdg wit="f1823">entreat, and I</rdg>
			<rdg wit="fThomas">entreat, and I</rdg>
			<rdg wit="f1831">entreat, and I</rdg>
		</rdgGr
    ```		
    - 2023-7-14: I added a space between "you" and "&"
- [ ] misalignment found
    ```
	<app>
		<rdgGrp n="['words,']">
			<rdg wit="f1818">words,</rdg>
			<rdg wit="f1823">words,</rdg>
			<rdg wit="fThomas">words,</rdg>
			<rdg wit="f1831">words,</rdg>
		</rdgGrp>
		<rdgGrp n="['words–', 'i']">
			<rdg wit="fMS">words– &lt;shi rend="underline"&gt;I</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['&#34; i']">
			<rdg wit="f1818">“&lt;hi sID="novel1_letter4_chapter21_div4_div23_p31_hi1"/&gt;I</rdg>
			<rdg wit="f1823">“&lt;hi sID="novel1_letter4_chapter21_div4_div22_p30_hi1"/&gt;I</rdg>
			<rdg wit="fThomas">“&lt;hi sID="novel1_letter4_chapter21_div4_div23_p31_hi1"/&gt;I</rdg>
		</rdgGrp>
		<rdgGrp n="['&#34;i']">
			<rdg wit="f1831">“I</rdg>
		</rdgGrp>
	</app>
    ```	
    - I wrapped "i shall be" in all versions 
        - Did not work. Manuscript version needs to be pulled up to next app in order to align properly. That, all the other versions except the manuscript get pushed down.
    - 2023-7-19: I wrapped "i shall be" in all versions, ignoring quotaton mark
- [ ] 2023-7-14: transdisposition found
    ```
	<app>
		<rdgGrp n="['if', 'my', 'cousin', 'would', 'consent,']">
			<rdg wit="f1818">if my cousin would consent,</rdg>
			<rdg wit="f1823">if my cousin would consent,</rdg>
			<rdg wit="fThomas">if my cousin would consent,</rdg>
			<rdg wit="f1831">if my cousin would consent,</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['the', 'ceremony', 'should', 'take', 'place']">
			<rdg wit="f1818">the ceremony should take place</rdg>
			<rdg wit="f1823">the ceremony should take place</rdg>
			<rdg wit="fThomas">the ceremony should take place</rdg>
			<rdg wit="f1831">the ceremony should take place</rdg>
			<rdg wit="fMS">the ceremony &lt;lb n="c57-0142__main__11"/&gt;should take place</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['in', 'ten']">
			<rdg wit="f1818">in ten</rdg>
			<rdg wit="f1823">in ten</rdg>
			<rdg wit="fThomas">in ten</rdg>
			<rdg wit="f1831">in ten</rdg>
		</rdgGrp>
		<rdgGrp n="['if', 'my', 'cousin', 'would', 'consent', 'in', 'ten']">
			<rdg wit="fMS">if my cousin would &lt;lb n="c57-0142__main__12"/&gt;consent in ten</rdg>
		</rdgGrp>
	</app>

    ```
    - wrapped longToken around all versions of "that if my cousin would consent, the ceremony should take place in ten days" and "that the ceremony should take place if my cousin would consent in ten days."
        - Did not work. I think I just need to move the first longToken before "father" for all the other versions to be properly aligned.
- [ ] misalignment 
    ```
	<app>
		<rdgGrp n="['']">
			<rdg wit="fMS">&lt;sga-add eID="c57-0144__main__d4e26858"/&gt;&lt;mod
				eID="c57-0144__main__d4e26850"/&gt;</rdg>
		</rdgGrp>
		<rdgGrp n="['secret,']">
			<rdg wit="f1818">secret,</rdg>
			<rdg wit="f1823">secret,</rdg>
			<rdg wit="fThomas">secret,</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['secret']">
			<rdg wit="f1831">secret</rdg>
			<rdg wit="fMS">secret</rdg>
		</rdgGrp>
	</app>
    ```	
    - Removed space before secret in manuscript. idk if this will work   
    - 2023-07-19: Wrapped "dreadful secret" in all versions.
- [ ] large misalignmet found for 1831. 
    ```
	<app>
		<rdgGrp n="['a']">
			<rdg wit="f1818">A</rdg>
			<rdg wit="f1823">A</rdg>
			<rdg wit="fThomas">A</rdg>
			<rdg wit="fMS">A</rdg>
		</rdgGrp>
		<rdgGrp n="['through', 'my', 'father’s', 'exertions,', 'a']">
			<rdg wit="f1831">Through my father’s exertions, a</rdg>
		</rdgGrp>
	</app>

	<app>
		<rdgGrp n="['house', 'was', 'purchased', 'for', 'us', 'near']">
			<rdg wit="f1818">house was purchased for us near</rdg>
			<rdg wit="f1823">house was purchased for us near</rdg>
			<rdg wit="fThomas">house was purchased for us near</rdg>
			<rdg wit="fMS">house was purchased for us &lt;lb n="c57-0143__main__14"/&gt;near</rdg>
		</rdgGrp>
		<rdgGrp
			n="['part', 'of', 'the', 'inheritance', 'of', 'elizabeth', 'had', 'been', 'restored', 'to', 'her']">
			<rdg wit="f1831">part of the inheritance of Elizabeth had been restored to her</rdg>
		</rdgGrp>
	</app>
    ```
    - 2023-07-19: Wrapped large longToken around differing 1931 segment. 
- [ ] 2023-07-19: Weird alignment
    ```
    	<app>
		<rdgGrp
			n="['&lt;del&gt;,&lt;/del&gt;', '.', '&lt;del&gt;and return to cologny the next morning.&lt;/del&gt;']">
			<rdg wit="fThomas">&lt;del rend="strikethrough"&gt;,&lt;/del&gt;
				&lt;add&gt;.&lt;/add&gt; &lt;del&gt;and return to Cologny the next
				morning.&lt;/del&gt;</rdg>
		</rdgGrp>
		<rdgGrp n="['and']">
			<rdg wit="f1818">and</rdg>
			<rdg wit="f1823">and</rdg>
			<rdg wit="f1831">and</rdg>
			<rdg wit="fMS">and</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['continuing']">
			<rdg wit="f1831">continuing</rdg>
		</rdgGrp>
		<rdgGrp n="['return', 'to', 'cologny']">
			<rdg wit="f1818">return to Cologny</rdg>
			<rdg wit="f1823">return to Cologny</rdg>
		</rdgGrp>
		<rdgGrp n="['set', 'out', 'on']">
			<rdg wit="fMS">set out on</rdg>
		</rdgGrp>
	</app>
    ```
    - Wrapped longToken around "Evian, and continuing our voyage on the following day. The day was" in all versions   
## pass 2
- [ ] "To Victor Frankenstein, my dearest friend" aligned inappropriately.
    ```
	<app>
		<rdgGrp n="['&#34; to', 'v ictor', 'f rankenstein .', '&lt;p-end/&gt;']">
			<rdg wit="f1818">“&lt;hi sID="novel1_letter4_chapter21_div4_div23_p11_hi1"/&gt;To&lt;hi
				eID="novel1_letter4_chapter21_div4_div23_p11_hi1"/&gt; V&lt;hi
				sID="novel1_letter4_chapter21_div4_div23_p11_hi2"/&gt;ICTOR&lt;hi
				eID="novel1_letter4_chapter21_div4_div23_p11_hi2"/&gt; F&lt;hi
				sID="novel1_letter4_chapter21_div4_div23_p11_hi3"/&gt;RANKENSTEIN&lt;hi
				eID="novel1_letter4_chapter21_div4_div23_p11_hi3"/&gt;. &lt;p
				eID="novel1_letter4_chapter21_div4_div23_p11"/&gt;</rdg>
			<rdg wit="f1823">“&lt;hi sID="novel1_letter4_chapter21_div4_div22_p10_hi1"/&gt;To&lt;hi
				eID="novel1_letter4_chapter21_div4_div22_p10_hi1"/&gt; V&lt;hi
				sID="novel1_letter4_chapter21_div4_div22_p10_hi2"/&gt;ICTOR&lt;hi
				eID="novel1_letter4_chapter21_div4_div22_p10_hi2"/&gt; F&lt;hi
				sID="novel1_letter4_chapter21_div4_div22_p10_hi3"/&gt;RANKENSTEIN&lt;hi
				eID="novel1_letter4_chapter21_div4_div22_p10_hi3"/&gt;. &lt;p
				eID="novel1_letter4_chapter21_div4_div22_p10"/&gt;</rdg>
			<rdg wit="fThomas">“&lt;hi
				sID="novel1_letter4_chapter21_div4_div23_p11_hi1"/&gt;To&lt;hi
				eID="novel1_letter4_chapter21_div4_div23_p11_hi1"/&gt; V&lt;hi
				sID="novel1_letter4_chapter21_div4_div23_p11_hi2"/&gt;ICTOR&lt;hi
				eID="novel1_letter4_chapter21_div4_div23_p11_hi2"/&gt; F&lt;hi
				sID="novel1_letter4_chapter21_div4_div23_p11_hi3"/&gt;RANKENSTEIN&lt;hi
				eID="novel1_letter4_chapter21_div4_div23_p11_hi3"/&gt;. &lt;p
				eID="novel1_letter4_chapter21_div4_div23_p11"/&gt;</rdg>
		</rdgGrp>
		<rdgGrp
			n="['to', 'victor', 'fankenstein', 'may', '', '&lt;del&gt;feb.&lt;/del&gt;', '', '18', '–', '17—', 'my', 'dearest', 'friend.', 'it']">
			<rdg wit="fMS">&lt;lb n="c57-0134__main__33"/&gt;To Victor Fankenstein &lt;lb
				n="c57-0134__main__34"/&gt;&lt;mod sID="c57-0134__main__d4e25000"/&gt;&lt;sga-add
				place="superlinear" sID="c57-0134__main__d4e25002"/&gt;May &lt;sga-add
				eID="c57-0134__main__d4e25002"/&gt; &lt;del rend="strikethrough"
				xml:id="c57-0134__main__d4e25005"&gt;Feb.&lt;/del&gt; &lt;mod
				eID="c57-0134__main__d4e25000"/&gt; 18 – 17— &lt;lb n="c57-0134__main__35"/&gt;My
				dearest Friend. &lt;lb n="c57-0135__main__1"/&gt;It</rdg>
		</rdgGrp>
	</app>
    ```
    - Wrapped longToken around all versions of "To Victor Frankenstein, my dearest friend"