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
- [X] misalignment found
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
- [X] misalignment found
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
- [X] 2023-7-14: transdisposition found
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
- [X] misalignment 
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
- [X] large misalignmet found for 1831. 
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
    - 2023-07-19: I also wrapped the other editions, "A house was purchased for us near Cologny, by which we should enjoy the pleasures of the country, and yet be so near Geneva as to see my father every day; who would still reside within the walls, for the benefit of Ernest, that he might follow his studies at the schools."
        - Really the previous longToken worked, but then we have a section marked blue. It is annoying.
- [X] 2023-07-19: Weird alignment
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
- [X] "To Victor Frankenstein, my dearest friend" aligned inappropriately.
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
- [X] misalignment, we should be in next app
    ```
    	<app>
		<rdgGrp n="['infancy.']">
			<rdg wit="f1818">infancy.</rdg>
			<rdg wit="fThomas">infancy.</rdg>
			<rdg wit="f1831">infancy.</rdg>
		</rdgGrp>
		<rdgGrp n="['infancy–we']">
			<rdg wit="fMS">infancy–We</rdg>
		</rdgGrp>
		<rdgGrp n="['intimacy.']">
			<rdg wit="f1823">intimacy.</rdg>
		</rdgGrp>
	</app>
    ```
    - added space before we in manuscript 
- [X] misalignment. "ah victor" should be in following app
    ```
    	<app>
		<rdgGrp n="['wishes', 'ah', 'victor']">
			<rdg wit="fMS">wishes &lt;lb n="c57-0137__main__15"/&gt;Ah Victor</rdg>
		</rdgGrp>
		<rdgGrp n="['wishes.']">
			<rdg wit="f1818">wishes.</rdg>
			<rdg wit="f1823">wishes.</rdg>
			<rdg wit="fThomas">wishes.</rdg>
			<rdg wit="f1831">wishes.</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['ah!']">
			<rdg wit="f1831">Ah!</rdg>
		</rdgGrp>
		<rdgGrp n="['ah,']">
			<rdg wit="f1818">Ah,</rdg>
			<rdg wit="f1823">Ah,</rdg>
			<rdg wit="fThomas">Ah,</rdg>
		</rdgGrp>
	</app>
    ```
    - Wrapped longToken around all versions of "ah victor"
        - did not work. moving first longToken before wishes
- [X] misalignment
    ```
    	<app>
		<rdgGrp n="['it']">
			<rdg wit="f1818">it</rdg>
			<rdg wit="f1823">it</rdg>
			<rdg wit="fThomas">it</rdg>
			<rdg wit="fMS">it</rdg>
		</rdgGrp>
		<rdgGrp n="['tomorrow,']">
			<rdg wit="f1831">tomorrow,</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['to-morrow,']">
			<rdg wit="f1818">to-morrow,</rdg>
			<rdg wit="f1823">to-morrow,</rdg>
			<rdg wit="fThomas">to-morrow,</rdg>
		</rdgGrp>
		<rdgGrp n="['tomorrow']">
			<rdg wit="fMS">tomorrow</rdg>
		</rdgGrp>
	</app>
    ```    
    - 2023-7-19: wrapped all versions of "not answer it to-morrow, or the next day," in longToken    
    
- [x] 2023-7-19: Not a misalignment but is marked yellow. it is annoying.

    ```
    	<app>
		<rdgGrp n="['spoke', 'or']">
			<rdg wit="f1818">spoke or</rdg>
			<rdg wit="fThomas">spoke or</rdg>
			<rdg wit="fMS">spoke or</rdg>
		</rdgGrp>
		<rdgGrp n="['spoke,', 'nor']">
			<rdg wit="f1823">spoke, nor</rdg>
			<rdg wit="f1831">spoke, nor</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['looked']">
			<rdg wit="f1823">looked</rdg>
			<rdg wit="f1831">looked</rdg>
			<rdg wit="fMS">looked</rdg>
		</rdgGrp>
		<rdgGrp n="['looked,']">
			<rdg wit="f1818">looked,</rdg>
			<rdg wit="fThomas">looked,</rdg>
		</rdgGrp>
	</app>
    ```
    - Wrapped longToken around all versions of 'I neither spoke or looked, but sat'    

- [x] Misalignment

    ```
	<app>
		<rdgGrp n="['', 'tranquillity–', 'and', 'indeed']">
			<rdg wit="fMS">&lt;sga-add eID="c57-0143__main__d4e26688"/&gt;&lt;mod
				eID="c57-0143__main__d4e26680"/&gt; tranquillity– And indeed</rdg>
		</rdgGrp>
		<rdgGrp n="['&lt;del&gt;tranquillity&lt;/del&gt;', 'security', '.']">
			<rdg wit="fThomas">&lt;del rend="strikethrough"&gt;tranquillity&lt;/del&gt;
				&lt;add&gt;security&lt;/add&gt; .</rdg>
		</rdgGrp>
		<rdgGrp n="['tranquillity.']">
			<rdg wit="f1818">tranquillity.</rdg>
			<rdg wit="f1823">tranquillity.</rdg>
			<rdg wit="f1831">tranquillity.</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['indeed,']">
			<rdg wit="f1818">Indeed,</rdg>
			<rdg wit="f1823">Indeed,</rdg>
			<rdg wit="fThomas">Indeed,</rdg>
			<rdg wit="f1831">Indeed,</rdg>
		</rdgGrp>
	</app>
    ```	
    - I wrapped a longToken around all versions of "gained a greater degree of tranquillity. Indeed,"    

- [x] Misalignment

    ```
		<rdgGrp n="['overjoyed', 'and']">
			<rdg wit="fMS">&lt;w ana="start"/&gt;over&lt;lb n="c57-0144__main__9"/&gt;joyed&lt;w
				ana="end"/&gt; and</rdg>
		</rdgGrp>
		<rdgGrp n="['overjoyed,']">
			<rdg wit="f1823">overjoyed,</rdg>
			<rdg wit="f1831">overjoyed,</rdg>
		</rdgGrp>
		<rdgGrp n="['overjoyed;']">
			<rdg wit="f1818">overjoyed;</rdg>
			<rdg wit="fThomas">overjoyed;</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['and,']">
			<rdg wit="f1818">and,</rdg>
			<rdg wit="f1823">and,</rdg>
			<rdg wit="fThomas">and,</rdg>
			<rdg wit="f1831">and,</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['in', 'the', 'bustle', 'of']">
			<rdg wit="f1818">in the bustle of</rdg>
			<rdg wit="f1823">in the bustle of</rdg>
			<rdg wit="fThomas">in the bustle of</rdg>
			<rdg wit="f1831">in the bustle of</rdg>
			<rdg wit="fMS">in the bustle of</rdg>
		</rdgGrp>
	</app>
    ```
    - Wrapped longToken around all versions of "overjoyed, and, in the bustle of"    

- [X] Misalignment
    ```
	<app>
		<rdgGrp n="['&lt;del&gt;pass the afternoon and night&lt;/del&gt;']">
			<rdg wit="fThomas">&lt;del rend="strikethrough"&gt;pass the afternoon and
				night&lt;/del&gt;</rdg>
		</rdgGrp>
		<rdgGrp n="['commence', 'our', 'journey', 'by', 'water,', 'sleeping', 'that']">
			<rdg wit="f1831">commence our journey by water, sleeping that</rdg>
		</rdgGrp>
		<rdgGrp n="['pass', 'the', 'afternoon', 'and']">
			<rdg wit="f1818">pass the afternoon and</rdg>
			<rdg wit="f1823">pass the afternoon and</rdg>
			<rdg wit="fMS">pass the afternoon &amp;</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['night']">
			<rdg wit="f1818">night</rdg>
			<rdg wit="f1823">night</rdg>
			<rdg wit="f1831">night</rdg>
			<rdg wit="fMS">night</rdg>
		</rdgGrp>
	</app>
    ```	
    - Wrapped longToken around "pass the afternoon and night"    

