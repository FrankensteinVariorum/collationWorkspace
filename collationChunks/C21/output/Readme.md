# Collation Chunk-21:

## Notes
- the marked boxes are solved/correct changes. unmarked boxes are unsolved
- the remaining blue marks when checking collation  are likely valid and dont need to be changed. Or they are one of the unmarked problems that can be found below.
- There are probably some misalignments I missed not found by the schema.
                
## Changes:
- [x] weird misalignment around this rdgGroup? cannot figure out where it starts and ends. need peer review.
  **2023-05-26 ebb** No problem here: This is correctly aligned--the MS witness just doesn't share this passage with the other witnesses. 

    - ```xml
  	<rdgGrp
  		n="['limb', 'from', 'limb,', 'as', 'the', 'lion', 'rends', 'the', 'antelope.', 'but', 'my', 'heart', 'sunk', 'within', 'me', 'as', 'with', 'bitter', 'sickness,', 'and', 'i', 'refrained.', 'i', 'saw', 'him']">
  		<rdg wit="f1818">limb from limb, as the lion rends the antelope. But my heart sunk
  			within me as with bitter sickness, and I refrained. I saw him</rdg>
  		<rdg wit="f1823">limb from limb, as the lion rends the antelope. But my heart sunk
  			within me as with bitter sickness, and I refrained. I saw him</rdg>
  		<rdg wit="fThomas">limb from limb, as the lion rends the antelope. But my heart sunk
  			within me as with bitter sickness, and I refrained. I saw him</rdg>
  		<rdg wit="f1831">limb from limb, as the lion rends the antelope. But my heart sunk
  			within me as with bitter sickness, and I refrained. I saw him</rdg>
  	</rdgGrp>
      ```

- [X] misalignment. all the "I" after "protectors" are in next app, for all versions aside from manuscript
    - wrapped longToken around "protectors—" in manuscript
    - ```xml
    	<app>
    		<rdgGrp n="['protectors.']">
    			<rdg wit="f1818">protectors.</rdg>
    			<rdg wit="f1823">protectors.</rdg>
    			<rdg wit="fThomas">protectors.</rdg>
    			<rdg wit="f1831">protectors.</rdg>
    		</rdgGrp>
    		<rdgGrp n="['protectors—i']">
    			<rdg wit="fMS">protectors—I</rdg>
    		</rdgGrp>
    	</app>
      ```
      

- [X] "full" not in one token
    - removed space after ful in manuscript
    - ```xml
		<rdg wit="fMS">ful &lt;sga-add place="intralinear"
				sID="c57-0047__main__d4e9172"/&gt;l</rdg>
		</rdgGrp>
      ```
      

- [x] in manuscript, the quote is misaligned I think. the dialogue/quote starts in next app for all the other versions.
    - need peer review help
    
	- **2023-05-29 yxj** wrapped longToken around `I: ‘I` in 1831
	
	- ```xml
    	<rdgGrp n="['i–', '&#34;i']">
    		<rdg wit="fMS">I– "I</rdg>
    	</rdgGrp>
      ```
    
- [X] "renewed" is seperated. In different rdgGrp even though spelling and punctuation are consistent through out all versions.
    - removed space after "renew"
    - ```xml
		<rdgGrp n="['renew', 'ed', '', 'determination']">
			<rdg wit="fMS">&lt;lb n="c57-0046__main__19"/&gt;renew &lt;sga-add place="intralinear"
				sID="c57-0046__main__d4e8870"/&gt;ed &lt;sga-add eID="c57-0046__main__d4e8870"/&gt;
				determination</rdg>
		</rdgGrp>
      ```
    
- [X] "thought" is seperated and unneeded space.
    - removed space after though to put together. minor change. probably fine? making it look cleaner i guess
    - ```xml
		<rdgGrp n="['though', 't', '', 'therefore']">
			<rdg wit="fMS">though &lt;sga-add place="intralinear"
				sID="c57-0045__main__d4e8646"/&gt;t &lt;sga-add eID="c57-0045__main__d4e8646"/&gt;
				therefore</rdg>
		</rdgGrp>
      ```

- [x] misaligned. Everything after "are" are in different apps
    - I have no idea how to fix this section. Need peer review help
    - **2023-05-29 yxj** wrapped longToken around `Germans"– ... No –They are` in MS.
    - ```xml
    	<rdgGrp
    		n="['hopes.&#34;', '&#34;are', 'these', 'germans&#34;–', '&lt;del&gt; &lt;unclear extent=&#34;1&#34; unit=&#34;chars&#34;/&gt; &lt;/del&gt;', 'asked', 'de', 'lacey', '–', '&lt;del&gt;know&lt;/del&gt;', '&#34;no', '–they']">
    		<rdg wit="fMS">hopes." "Are these Germans"– &lt;del rend="strikethrough"
    			xml:id="c57-0047__main__d4e9070"&gt; &lt;unclear extent="1" unit="chars"/&gt;
    			&lt;/del&gt; Asked &lt;lb n="c57-0047__main__17"/&gt;De Lacey – &lt;del
    			instant="true" rend="strikethrough"
    			xml:id="c57-0047__main__d4e9077"&gt;know&lt;/del&gt; "No –They</rdg>
    	</rdgGrp>
	```

- [x] Misalligned. "me" and "and" are in the next app for other versions. Need peer review help
  
	- **2023-05-29 yxj** wrapped longToken around `abandoned me; and,` in 1831.
	
    ```xml
        <rdgGrp n="['abbandoned', 'me', 'and']">
            <rdg wit="fMS">abbandoned me and</rdg>
            </rdgGrp>
    ```

  

- [x] "cursed" and "creator" are misalligned. with next app. Need peer review help

    - backspaced until "creator" was on one line

    - wrapped "cursed" with longToken in MS

    - **2023-05-29 yxj** wrapped longToken around `agony. ‘Accursed creator!` in 1831.

    - ```xml
    	<rdgGrp n="['agony—', 'cursed', '', '&lt;mdel&gt;c&lt;/mdel&gt;', 'c', '', 'reator']">
    		<rdg wit="fMS">agony— Cursed &lt;mod sID="c57-0041__main__d4e7678"/&gt;
    			&lt;mdel&gt;c&lt;/mdel&gt; &lt;sga-add place="intralinear"
    			sID="c57-0041__main__d4e7682"/&gt;C &lt;sga-add
    			eID="c57-0041__main__d4e7682"/&gt;&lt;mod eID="c57-0041__main__d4e7678"/&gt;
    			reator</rdg>
    	</rdgGrp>
      ```

 - [x] In msColl_21, I backspaced the "a" and "s" characters to be on the same line.  Need peer review help. Other versions start with "As", but in next app. Misaligned? 

  -  **2023-05-29 yxj** wrapped longToken`<note resp="#ebb">Thomas copy: pencil mark joins paragraphs.</note> “As` in Thomas.

  - ```xml
    <rdgGrp n="['', '&lt;del&gt;but crimes were distant&lt;/del&gt;', '&lt;del&gt;but&lt;/del&gt;', '', '&lt;mdel&gt;a&lt;/mdel&gt;', 'a', '', 's']">
    	<rdg wit="fMS">&lt;lb n="c57-0037__main__6"/&gt; &lt;del rend="strikethrough" xml:id="c57-0037__main__d4e5934"&gt;But crimes were distant&lt;/del&gt; &lt;del instant="true" rend="strikethrough" xml:id="c57-0037__main__d4e5938"&gt;But&lt;/del&gt; &lt;mod sID="c57-0037__main__d4e5941"/&gt; &lt;mdel&gt;a&lt;/mdel&gt; &lt;sga-add place="intralinear" sID="c57-0037__main__d4e5945"/&gt;A &lt;sga-add eID="c57-0037__main__d4e5945"/&gt;&lt;mod eID="c57-0037__main__d4e5941"/&gt; s</rdg></rdgGrp>

- [x] In Manuscript, I moved the element to be on the same line as the letter

    - ```xml
    	<rdgGrp n="['i', '', '&lt;mdel&gt;e&lt;/mdel&gt;', 'i']">
    		<rdg wit="fMS">I &lt;lb n="c57-0038__main__20"/&gt;&lt;mod
    		sID="c57-0038__main__d4e6490"/&gt; &lt;mdel&gt;e&lt;/mdel&gt; &lt;sga-add
    		place="intralinear" sID="c57-0038__main__d4e6494"/&gt;i</rdg>
    	</rdgGrp>
      ```

- [x] app has &lt; three reading witnesses, BUT looks valid  to the according files. Wrapped longToken around "to the beings concerning whom I" in according editions
    - ```xml
        <rdgGrp n="['to']">
           <rdg wit="f1823">to</rdg>
           <rdg wit="f1831">to</rdg>
       </rdgGrp>
       ```

- [x] "peaceable lawgivers" in a single witness, while the other versions have "peacable" & "lawgivers" in different apps.
    - ```xml
        <app>
          <rdgGrp n="['peacable', 'lawgivers']">
             <rdg wit="fMS">peacable &lt;lb n="c57-0039__main__29"/&gt;lawgivers</rdg>
          </rdgGrp>
          <rdgGrp n="['peaceable']">
              <rdg wit="f1818">peaceable</rdg>
              <rdg wit="f1823">peaceable</rdg>
              <rdg wit="fThomas">peaceable</rdg>
              <rdg wit="f1831">peaceable</rdg>
           </rdgGrp>
        </app>
        ```

- [x] "plutarchs's lives", the title of the book is weirdly mixed up with other wirtnesses?
    - ```xml
    	<rdgGrp n="[&#34;plutarch's&#34;]">
    		<rdg wit="f1823">&lt;hi
    			sID="novel1_letter4_chapter14_div4_div15_p3_hi2"/&gt;Plutarch's</rdg>
    	</rdgGrp>
    	<rdgGrp n="['plutarchs', 'lives']">
    		<rdg wit="fMS">Plutarchs &lt;lb n="c57-0037__main__28"/&gt;lives</rdg>
    	</rdgGrp>
    	<rdgGrp n="['plutarch’s']">
    		<rdg wit="f1818">&lt;hi
    			sID="novel1_letter4_chapter14_div4_div15_p3_hi2"/&gt;Plutarch’s</rdg>
    		<rdg wit="fThomas">&lt;hi
    			sID="novel1_letter4_chapter14_div4_div15_p2_hi2"/&gt;Plutarch’s</rdg>
    	</rdgGrp>
    	<rdgGrp n="['‘plutarch’s', 'lives,’']">
    		<rdg wit="f1831">‘Plutarch’s Lives,’</rdg>
    	</rdgGrp>
    	```


- [x] "benevolenceand" in MS is muddled. It combines the word "benevolence" with "and".

  ```xml
  <rdgGrp
  			n="['', '&lt;del&gt;but&lt;/del&gt;', '&lt;del&gt; for  &lt;/del&gt;', 'benevolenceand']">
  			<rdg wit="fMS">&lt;mod sID="c57-0037__main__d4e5951"/&gt; &lt;del rend="strikethrough"
  				xml:id="c57-0037__main__d4e5953"&gt;but&lt;/del&gt; &lt;del rend="strikethrough"
  				xml:id="c57-0037__main__d4e5956"&gt; &lt;sga-add place="superlinear"
  				sID="c57-0037__main__d4e5958"/&gt;for &lt;sga-add eID="c57-0037__main__d4e5958"/&gt;
  				&lt;/del&gt; &lt;mod eID="c57-0037__main__d4e5951"/&gt;&lt;w
  				ana="start"/&gt;bene&lt;lb n="c57-0037__main__8"/&gt;volence&lt;w
  				ana="end"/&gt;&amp;</rdg>
  		</rdgGrp>
  ```

  In the MS full flat file, it looks like this: `<w ana="start"/>bene<lb n="c57-0037__main__8"/>volence<w ana="end"/> &amp; `. The space after the end tag of `w` is ignored in tokenization in the partway file for some reason. 


- [x] Muddled combination in MS: `unfortunateand` 

  ```xml
  <rdgGrp n="['unfortunateand']">
      <rdg wit="fMS">&lt;w ana="start"/&gt;unfortu&lt;lb n="c57-0047__main__19"/&gt;nate&lt;w
          ana="pullend"/&gt;&amp;</rdg>
  </rdgGrp>
  ```


  - There is no space after `unfortunate`:

  ```xml
  I am unfortunate
   and <lb n="c57-0047__main__13"/>a Str

  ```

- [x] ### Less than 5 rdgs:

- [x] ```xml
  <!-- search `Fortunately the books` to locate -->
  <app>
      <rdgGrp n="['fortunately']">
          <rdg wit="f1818">Fortunately</rdg>
          <rdg wit="f1823">Fortunately</rdg>
          <rdg wit="fThomas">Fortunately</rdg>
          <rdg wit="f1831">Fortunately</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['created']">
          <rdg wit="f1818">created</rdg>
          <rdg wit="fThomas">created</rdg>
      </rdgGrp>
      <rdgGrp n="['', '&lt;del&gt;self&lt;/del&gt;', '', 'created']">
          <rdg wit="fMS">&lt;sga-add eID="c57-0040__main__d4e7182"/&gt;&lt;lb
              n="c57-0040__main__16"/&gt; &lt;del rend="strikethrough"
              xml:id="c57-0040__main__d4e7188"&gt;self&lt;/del&gt; &lt;anchor
              xml:id="c57-0040.05"/&gt; created</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <!-- search `far different` to locate -->
  <app>
      <rdgGrp n="['far']">
          <rdg wit="f1818">far</rdg>
          <rdg wit="f1823">far</rdg>
          <rdg wit="fThomas">far</rdg>
          <rdg wit="f1831">far</rdg>
      </rdgGrp>
  </app>
  ```

- [ ] ```xml
  <app>
      <rdgGrp
              n="['', '&lt;del&gt;but i would not disturb their&lt;/del&gt;', '', '&lt;del&gt; &lt;unclear extent=&#34;2&#34; unit=&#34;chars&#34;/&gt;he&lt;/del&gt;']">
          <rdg wit="fMS">&lt;lb n="c57-0040__main__29"/&gt; &lt;del rend="strikethrough"
              xml:id="c57-0040__main__d4e7319"&gt;But I would not disturb their&lt;/del&gt; &lt;lb
              n="c57-0040__main__30"/&gt; &lt;del rend="strikethrough"
              xml:id="c57-0040__main__d4e7324"&gt; &lt;unclear extent="2"
              unit="chars"/&gt;he&lt;/del&gt;</rdg>
      </rdgGrp>
      <rdgGrp
              n="['while neither the feeling of remorse of self accusation mingled with my throes; although the contempt with i was treated also prevented any sublime defiance to have a place in my mind.']">
          <rdg wit="fThomas">&lt;add place="bottom"&gt;While neither the feeling of remorse of
              self accusation mingled with my throes; although the contempt with I was treated
              also prevented any sublime defiance to have a place in my mind.&lt;/add&gt;</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['more', 'horrid']">
          <rdg wit="f1818">more horrid</rdg>
          <rdg wit="f1823">more horrid</rdg>
          <rdg wit="fThomas">more horrid</rdg>
          <rdg wit="f1831">more horrid</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['even']">
          <rdg wit="f1823">even</rdg>
          <rdg wit="f1831">even</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['from']">
          <rdg wit="f1818">from</rdg>
          <rdg wit="f1823">from</rdg>
          <rdg wit="fThomas">from</rdg>
          <rdg wit="f1831">from</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['with', 'them']">
          <rdg wit="f1818">with them</rdg>
          <rdg wit="f1823">with them</rdg>
          <rdg wit="fThomas">with them</rdg>
          <rdg wit="f1831">with them</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp
              n="['even', 'as', 'that', 'frail', 'image', 'and', 'that', 'inconstant', 'shade.', '&lt;p-end/&gt;', '&lt;p-start/&gt;', '&#34;i']">
          <rdg wit="f1818">even as that frail image and that inconstant shade. &lt;p
              eID="novel1_letter4_chapter14_div4_div15_p10"/&gt; &lt;p
              sID="novel1_letter4_chapter14_div4_div15_p11"/&gt; “I</rdg>
          <rdg wit="f1823">even as that frail image and that inconstant shade. &lt;p
              eID="novel1_letter4_chapter14_div4_div15_p10"/&gt; &lt;p
              sID="novel1_letter4_chapter14_div4_div15_p11"/&gt; “I</rdg>
          <rdg wit="fThomas">even as that frail image and that inconstant shade. &lt;p
              eID="novel1_letter4_chapter14_div4_div15_p9"/&gt; &lt;p
              sID="novel1_letter4_chapter14_div4_div15_p10"/&gt; “I</rdg>
          <rdg wit="f1831">even as that frail image and that inconstant shade. &lt;p
              eID="novel1_letter4_chapter15_div4_div15_p10"/&gt; &lt;p
              sID="novel1_letter4_chapter15_div4_div15_p11"/&gt; “I</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['worn']">
          <rdg wit="f1818">worn</rdg>
          <rdg wit="f1823">worn</rdg>
          <rdg wit="fThomas">worn</rdg>
          <rdg wit="f1831">worn</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['realise']">
          <rdg wit="f1831">realise</rdg>
      </rdgGrp>
      <rdgGrp n="['realize']">
          <rdg wit="f1818">realize</rdg>
          <rdg wit="f1823">realize</rdg>
          <rdg wit="fThomas">realize</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['my', 'fears.']">
          <rdg wit="f1818">my fears.</rdg>
          <rdg wit="f1823">my fears.</rdg>
          <rdg wit="fThomas">my fears.</rdg>
          <rdg wit="f1831">my fears.</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <!-- search `when unprejudiced by` to locate -->
  <app>
      <rdgGrp n="['any']">
          <rdg wit="f1818">any</rdg>
          <rdg wit="f1823">any</rdg>
          <rdg wit="fThomas">any</rdg>
          <rdg wit="f1831">any</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['of', 'your', 'tale,']">
          <rdg wit="f1818">of your tale,</rdg>
          <rdg wit="f1823">of your tale,</rdg>
          <rdg wit="fThomas">of your tale,</rdg>
          <rdg wit="f1831">of your tale,</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['yet']">
          <rdg wit="f1818">Yet</rdg>
          <rdg wit="f1823">Yet</rdg>
          <rdg wit="fThomas">Yet</rdg>
          <rdg wit="f1831">Yet</rdg>
      </rdgGrp>
  </app>
  ```
