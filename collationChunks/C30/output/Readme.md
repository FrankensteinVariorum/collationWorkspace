## Hand fix

- delete space between `i` and `t` which seperate by `hi` element. 

  ```xml
  <app>
      <rdgGrp n="[&#34;chap. 17   it was eight o'clock&#34;]">
          <rdg wit="fMS">&lt;longToken&gt;Chap. 17 &lt;anchor xml:id="c57-0147.07"/&gt; &lt;lb
              n="c57-0147__main__2"/&gt;It was eight o'clock&lt;/longToken&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['chapter vi. &lt;p-start/&gt;i t  was eight o’clock']">
          <rdg wit="f1818">&lt;longToken&gt;&lt;head&gt;CHAPTER VI.&lt;/head&gt; &lt;p
              sID="novel1_letter4_chapter22_div4_div24_p1"/&gt;I&lt;hi
              sID="novel1_letter4_chapter22_div4_div24_p1_hi1"/&gt;T&lt;hi
              eID="novel1_letter4_chapter22_div4_div24_p1_hi1"/&gt; was eight
              o’clock&lt;/longToken&gt;</rdg>
          <rdg wit="fThomas">&lt;longToken&gt;&lt;head&gt;CHAPTER VI.&lt;/head&gt; &lt;p
              sID="novel1_letter4_chapter22_div4_div24_p1"/&gt;I&lt;hi
              sID="novel1_letter4_chapter22_div4_div24_p1_hi1"/&gt;T&lt;hi
              eID="novel1_letter4_chapter22_div4_div24_p1_hi1"/&gt; was eight
              o’clock&lt;/longToken&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['chapter xi. &lt;p-start/&gt;i t  was eight o’clock']">
          <rdg wit="f1823">&lt;longToken&gt;&lt;head&gt;CHAPTER XI.&lt;/head&gt; &lt;p
              sID="novel1_letter4_chapter22_div4_div23_p1"/&gt;I&lt;hi
              sID="novel1_letter4_chapter22_div4_div23_p1_hi1"/&gt;T&lt;hi
              eID="novel1_letter4_chapter22_div4_div23_p1_hi1"/&gt; was eight
              o’clock&lt;/longToken&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['chapter xxiii. &lt;p-start/&gt;i t  was eight o’clock']">
          <rdg wit="f1831">&lt;longToken&gt;&lt;head&gt;CHAPTER XXIII.&lt;/head&gt; &lt;p
              sID="novel1_letter4_chapter23_div4_div23_p1"/&gt;I&lt;hi
              sID="novel1_letter4_chapter23_div4_div23_p1_hi1"/&gt;T&lt;hi
              eID="novel1_letter4_chapter23_div4_div23_p1_hi1"/&gt; was eight
              o’clock&lt;/longToken&gt;</rdg>
      </rdgGrp>
  </app>
  ```

### app with less than 5 rdgs

- [x] Long texts in Thomas are wrapped in `<del>` and `<add>` which are treated as `<longToken>`. As such, several apps miss`<rdg>` for  Thomas. Search `inn` to check out the last `<app>` with less 5 rdgs caused by this problem. 

```xml
<app>
    <rdgGrp
            n="['&lt;del&gt;we walked for a short time on the shore, enjoying the transitory light, and then retired to the inn,&lt;/del&gt;', 'leaving the shore we sought the retreat of our house and garden. &lt;del&gt;but&lt;/del-inner&gt; &lt;del&gt;a&lt;/del-inner&gt;again as i entered the iron gates of the demesne, an &lt;del&gt;unres&lt;/del-inner&gt; unexplainable feeling bade me hold—yet elizabeth unwarned, and fearless passed on, and i, again half ashamed—and for the first time dreading lest any unholy sight should meet her sense, any shadow of the fiend, should cross her, &lt;del&gt;i&lt;/del-inner&gt; hastily walked on, and passing my arm round her prayed with a feeling of bitter tenderness, that she might never suffer ill. thus we entered the &lt;del&gt;ar&lt;/del-inner&gt; mansion—and still not speaking, for both our hearts were too full, we went to a balcony that overhung the lake']">
        <rdg wit="fThomas">&lt;del rend="strikethrough"&gt;we walked for a short time on the
            shore, enjoying the transitory light, and then retired to the inn,&lt;/del&gt;
            &lt;add place="bottom_and_following_page"&gt;leaving the shore we sought the retreat
            of our house and garden. &lt;del-INNER rend="strikethrough"&gt;but&lt;/del-INNER&gt;
            &lt;del-INNER rend="overwritten"&gt;a&lt;/del-INNER&gt;Again as I entered the iron
            gates of the demesne, an &lt;del-INNER&gt;unres&lt;/del-INNER&gt; unexplainable
            feeling bade me hold—yet Elizabeth &lt;pb n="117"/&gt;unwarned, and fearless passed
            on, and I, again half ashamed—&amp; for the first time dreading lest any unholy
            sight should meet her sense, any shadow of the fiend, should cross her,
            &lt;del-INNER&gt;I&lt;/del-INNER&gt; hastily walked on, and passing my arm round her
            prayed with a feeling of bitter tenderness, that she might never suffer ill. Thus we
            entered the &lt;del-INNER rend="strikethrough"&gt;ar&lt;/del-INNER&gt; mansion—and
            still not speaking, for both our hearts were too full, we went to a balcony that
            overhung the lake&lt;/add&gt;</rdg>
    </rdgGrp>
</app>
```

- [x] ```xml
  <app>
      <rdgGrp n="['a', 'heavy', 'storm', 'of', 'rain', 'descended.']">
          <rdg wit="f1818">a heavy storm of rain descended.</rdg>
          <rdg wit="f1823">a heavy storm of rain descended.</rdg>
          <rdg wit="fThomas">a heavy storm of rain descended.</rdg>
          <rdg wit="f1831">a heavy storm of rain descended.</rdg>
          <rdg wit="fMS">&lt;lb n="c57-0147__main__17"/&gt;a heavy storm of rain descended.</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&lt;p-end/&gt;']">
          <rdg wit="f1818">&lt;p eID="novel1_letter4_chapter22_div4_div24_p2"/&gt;</rdg>
          <rdg wit="f1823">&lt;p eID="novel1_letter4_chapter22_div4_div23_p2"/&gt;</rdg>
          <rdg wit="fThomas">&lt;p eID="novel1_letter4_chapter22_div4_div24_p2"/&gt;</rdg>
          <rdg wit="f1831">&lt;p eID="novel1_letter4_chapter23_div4_div23_p2"/&gt;</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['the']">
          <rdg wit="f1818">the</rdg>
          <rdg wit="f1823">the</rdg>
          <rdg wit="fThomas">the</rdg>
          <rdg wit="f1831">the</rdg>
          <rdg wit="fMS">the</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['impending']">
          <rdg wit="f1818">impending</rdg>
          <rdg wit="fThomas">impending</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['conflict']">
          <rdg wit="f1818">conflict</rdg>
          <rdg wit="f1823">conflict</rdg>
          <rdg wit="fThomas">conflict</rdg>
          <rdg wit="f1831">conflict</rdg>
          <rdg wit="fMS">conflict</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['she', 'said', '—', 'what', 'is', 'it,', 'my', 'dear', 'victor,']">
          <rdg wit="fMS">she said — What is it, my dear &lt;lb
              n="c57-0147__main__31"/&gt;Victor,</rdg>
      </rdgGrp>
      <rdgGrp n="['she']">
          <rdg wit="f1818">she</rdg>
          <rdg wit="f1823">she</rdg>
          <rdg wit="fThomas">she</rdg>
          <rdg wit="f1831">she</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['asked,']">
          <rdg wit="f1831">asked,</rdg>
      </rdgGrp>
      <rdgGrp n="['said,']">
          <rdg wit="f1818">said,</rdg>
          <rdg wit="f1823">said,</rdg>
          <rdg wit="fThomas">said,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&#34;what', 'is', 'it']">
          <rdg wit="f1818">“What is it</rdg>
          <rdg wit="f1823">“What is it</rdg>
          <rdg wit="fThomas">“What is it</rdg>
          <rdg wit="f1831">“What is it</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['and', 'tingling', 'in']">
          <rdg wit="f1818">and tingling in</rdg>
          <rdg wit="f1823">and tingling in</rdg>
          <rdg wit="fThomas">and tingling in</rdg>
          <rdg wit="f1831">and tingling in</rdg>
          <rdg wit="fMS">&lt;sga-add hand="#pbs" place="superlinear"
              sID="c57-0148__main__d4e27742"/&gt;&amp; tingling in</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['the', 'extremities', 'of']">
          <rdg wit="f1818">the extremities of</rdg>
          <rdg wit="f1823">the extremities of</rdg>
          <rdg wit="fThomas">the extremities of</rdg>
          <rdg wit="f1831">the extremities of</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['this', 'state', 'lasted', 'but']">
          <rdg wit="f1818">This state lasted but</rdg>
          <rdg wit="f1823">This state lasted but</rdg>
          <rdg wit="fThomas">This state lasted but</rdg>
          <rdg wit="f1831">This state lasted but</rdg>
          <rdg wit="fMS">&lt;sga-add eID="c57-0148__main__d4e27742"/&gt;&lt;mod
              eID="c57-0148__main__d4e27737"/&gt;&lt;lb n="c57-0148__main__23"/&gt;This state
              lasted but</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['for']">
          <rdg wit="f1818">for</rdg>
          <rdg wit="f1823">for</rdg>
          <rdg wit="fThomas">for</rdg>
          <rdg wit="f1831">for</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['and', 'i', 'rushed', 'into', 'the', 'room.']">
          <rdg wit="f1818">and I rushed into the room.</rdg>
          <rdg wit="f1823">and I rushed into the room.</rdg>
          <rdg wit="fThomas">and I rushed into the room.</rdg>
          <rdg wit="f1831">and I rushed into the room.</rdg>
          <rdg wit="fMS">&amp; I rushed &lt;lb n="c57-0148__main__25"/&gt;into the room.</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&lt;p-end/&gt;', '&lt;p-start/&gt;']">
          <rdg wit="f1818">&lt;p eID="novel1_letter4_chapter22_div4_div24_p7"/&gt; &lt;p
              sID="novel1_letter4_chapter22_div4_div24_p8"/&gt;</rdg>
          <rdg wit="f1823">&lt;p eID="novel1_letter4_chapter22_div4_div23_p7"/&gt; &lt;p
              sID="novel1_letter4_chapter22_div4_div23_p8"/&gt;</rdg>
          <rdg wit="fThomas">&lt;p eID="novel1_letter4_chapter22_div4_div24_p7"/&gt; &lt;p
              sID="novel1_letter4_chapter22_div4_div24_p8"/&gt;</rdg>
          <rdg wit="f1831">&lt;p eID="novel1_letter4_chapter23_div4_div23_p7"/&gt; &lt;p
              sID="novel1_letter4_chapter23_div4_div23_p8"/&gt;</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['&lt;del&gt;the people of the inn&lt;/del&gt;', 'servants', ';']">
          <rdg wit="fThomas">&lt;del rend="strikethrough"&gt;the people of the inn&lt;/del&gt;
              &lt;add place="margin"&gt;servants&lt;/add&gt; ;</rdg>
      </rdgGrp>
      <rdgGrp n="['the', 'people', 'of']">
          <rdg wit="f1818">the people of</rdg>
          <rdg wit="f1823">the people of</rdg>
          <rdg wit="f1831">the people of</rdg>
          <rdg wit="fMS">the people of</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['inn', '–']">
          <rdg wit="fMS">inn –</rdg>
      </rdgGrp>
      <rdgGrp n="['the', 'inn;']">
          <rdg wit="f1818">the inn;</rdg>
          <rdg wit="f1823">the inn;</rdg>
          <rdg wit="f1831">the inn;</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['deadly']">
          <rdg wit="f1823">deadly</rdg>
          <rdg wit="f1831">deadly</rdg>
      </rdgGrp>
      <rdgGrp n="['deathly']">
          <rdg wit="f1818">deathly</rdg>
          <rdg wit="fThomas">deathly</rdg>
          <rdg wit="fMS">&lt;lb n="c57-0149__main__21"/&gt;deathly</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['languor', 'and']">
          <rdg wit="f1818">languor and</rdg>
          <rdg wit="f1823">languor and</rdg>
          <rdg wit="fThomas">languor and</rdg>
          <rdg wit="f1831">languor and</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['the', 'windows', 'of']">
          <rdg wit="f1818">The windows of</rdg>
          <rdg wit="f1823">The windows of</rdg>
          <rdg wit="fThomas">The windows of</rdg>
          <rdg wit="f1831">The windows of</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['the', 'room']">
          <rdg wit="f1818">the room</rdg>
          <rdg wit="f1823">the room</rdg>
          <rdg wit="fThomas">the room</rdg>
          <rdg wit="f1831">the room</rdg>
          <rdg wit="fMS">The room</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['the', 'lake.']">
          <rdg wit="f1818">the lake.</rdg>
          <rdg wit="f1823">the lake.</rdg>
          <rdg wit="fThomas">the lake.</rdg>
          <rdg wit="f1831">the lake.</rdg>
          <rdg wit="fMS">the lake.</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&lt;p-end/&gt;', '&lt;p-start/&gt;']">
          <rdg wit="f1818">&lt;p eID="novel1_letter4_chapter22_div4_div24_p10"/&gt; &lt;p
              sID="novel1_letter4_chapter22_div4_div24_p11"/&gt;</rdg>
          <rdg wit="f1823">&lt;p eID="novel1_letter4_chapter22_div4_div23_p10"/&gt; &lt;p
              sID="novel1_letter4_chapter22_div4_div23_p11"/&gt;</rdg>
          <rdg wit="fThomas">&lt;p eID="novel1_letter4_chapter22_div4_div24_p10"/&gt; &lt;p
              sID="novel1_letter4_chapter22_div4_div24_p11"/&gt;</rdg>
          <rdg wit="f1831">&lt;p eID="novel1_letter4_chapter23_div4_div23_p10"/&gt; &lt;p
              sID="novel1_letter4_chapter23_div4_div23_p11"/&gt;</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['i', 'pointed', 'to']">
          <rdg wit="f1818">I pointed to</rdg>
          <rdg wit="f1823">I pointed to</rdg>
          <rdg wit="fThomas">I pointed to</rdg>
          <rdg wit="f1831">I pointed to</rdg>
          <rdg wit="fMS">&lt;lb n="c57-0150__main__13"/&gt;I pointed to</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['the', 'spot']">
          <rdg wit="f1818">the spot</rdg>
          <rdg wit="f1823">the spot</rdg>
          <rdg wit="fThomas">the spot</rdg>
          <rdg wit="f1831">the spot</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['it', 'to', 'have', 'been', 'a', 'form', 'conjured']">
          <rdg wit="f1818">it to have been a form conjured</rdg>
          <rdg wit="f1823">it to have been a form conjured</rdg>
          <rdg wit="fThomas">it to have been a form conjured</rdg>
          <rdg wit="f1831">it to have been a form conjured</rdg>
          <rdg wit="fMS">it to have &lt;lb n="c57-0150__main__18"/&gt;been a form conjured</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['up']">
          <rdg wit="f1823">up</rdg>
          <rdg wit="f1831">up</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['them', '&lt;del&gt;for']">
          <rdg wit="fMS">them &lt;lb n="c57-0150__main__23"/&gt;&lt;delSpan rend="strikethrough"
              spanTo="#c57-0150.01"/&gt;for</rdg>
      </rdgGrp>
      <rdgGrp n="['them,', 'and', 'proceeded', 'a', 'short', 'distance', 'from']">
          <rdg wit="f1831">them, and proceeded a short distance from</rdg>
      </rdgGrp>
      <rdgGrp n="['them;']">
          <rdg wit="f1818">them;</rdg>
          <rdg wit="f1823">them;</rdg>
          <rdg wit="fThomas">them;</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['the']">
          <rdg wit="f1831">the</rdg>
          <rdg wit="fMS">the</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['exhaustion', 'that', 'now', 'seized', 'on', 'me', '&lt;/del&gt;']">
          <rdg wit="fMS">exhaustion that now seized on &lt;lb n="c57-0150__main__24"/&gt;me
              &lt;delSpan anchor="c57-0150.01"/&gt;</rdg>
      </rdgGrp>
      <rdgGrp
              n="['house;', 'but', 'my', 'head', 'whirled', 'round,', 'my', 'steps', 'were', 'like', 'those', 'of', 'a', 'drunken', 'man,']">
          <rdg wit="f1831">house; but my head whirled round, my steps were like those of a drunken
              man,</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['that', 'i', 'had', 'lost.']">
          <rdg wit="f1818">that I had lost.</rdg>
          <rdg wit="f1823">that I had lost.</rdg>
          <rdg wit="fThomas">that I had lost.</rdg>
          <rdg wit="f1831">that I had lost.</rdg>
          <rdg wit="fMS">that I had lost.</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&lt;p-end/&gt;', '&lt;p-start/&gt;']">
          <rdg wit="f1818">&lt;p eID="novel1_letter4_chapter22_div4_div24_p12"/&gt; &lt;p
              sID="novel1_letter4_chapter22_div4_div24_p13"/&gt;</rdg>
          <rdg wit="f1823">&lt;p eID="novel1_letter4_chapter22_div4_div23_p12"/&gt; &lt;p
              sID="novel1_letter4_chapter22_div4_div23_p13"/&gt;</rdg>
          <rdg wit="fThomas">&lt;p eID="novel1_letter4_chapter22_div4_div24_p11"/&gt; &lt;p
              sID="novel1_letter4_chapter22_div4_div24_p12"/&gt;</rdg>
          <rdg wit="f1831">&lt;p eID="novel1_letter4_chapter23_div4_div23_p12"/&gt; &lt;p
              sID="novel1_letter4_chapter23_div4_div23_p13"/&gt;</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['elizabeth', 'and']">
          <rdg wit="f1818">Elizabeth and</rdg>
          <rdg wit="f1823">Elizabeth and</rdg>
          <rdg wit="fThomas">Elizabeth and</rdg>
          <rdg wit="fMS">Elizabeth &amp;</rdg>
      </rdgGrp>
      <rdgGrp
              n="['my', 'beloved', 'lay.', 'there', 'were', 'women', 'weeping', 'around—i', 'hung', 'over', 'it,', 'and', 'joined', 'my', 'sad']">
          <rdg wit="f1831">my beloved lay. There were women weeping around—I hung over it, and
              joined my sad</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['myself']">
          <rdg wit="fMS">myself</rdg>
      </rdgGrp>
      <rdgGrp n="['myself,']">
          <rdg wit="f1818">myself,</rdg>
          <rdg wit="f1823">myself,</rdg>
          <rdg wit="fThomas">myself,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp
              n="['and', 'that', 'i', 'must', 'return', 'alone.', 'this', 'reflection', 'brought']">
          <rdg wit="f1818">and that I must return alone. This reflection brought</rdg>
          <rdg wit="f1823">and that I must return alone. This reflection brought</rdg>
          <rdg wit="fThomas">and that I must return alone. This reflection brought</rdg>
          <rdg wit="fMS">&lt;lb n="c57-0150__main__32"/&gt;and that I must return alone. This
              &lt;lb n="c57-0150__main__33"/&gt;reflection brought</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['into', 'my']">
          <rdg wit="f1818">into my</rdg>
          <rdg wit="f1823">into my</rdg>
          <rdg wit="fThomas">into my</rdg>
          <rdg wit="fMS">into my</rdg>
      </rdgGrp>
      <rdgGrp
              n="['to', 'theirs—all', 'this', 'time', 'no', 'distinct', 'idea', 'presented', 'itself', 'to', 'my', 'mind;']">
          <rdg wit="f1831">to theirs—all this time no distinct idea presented itself to my
              mind;</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['eyes']">
          <rdg wit="fMS">eyes</rdg>
      </rdgGrp>
      <rdgGrp n="['eyes,']">
          <rdg wit="f1818">eyes,</rdg>
          <rdg wit="f1823">eyes,</rdg>
          <rdg wit="fThomas">eyes,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['and', 'i', 'wept', 'for', 'a', 'long']">
          <rdg wit="f1818">and I wept for a long</rdg>
          <rdg wit="f1823">and I wept for a long</rdg>
          <rdg wit="fThomas">and I wept for a long</rdg>
          <rdg wit="fMS">&amp; I &lt;lb n="c57-0150__main__34"/&gt;wept for a long</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['time.', 'i', 'reflected', 'o', '', '&lt;mdel&gt; &lt;/mdel&gt;', 'n', '']">
          <rdg wit="fMS">time. I reflected o &lt;mod sID="c57-0150__main__d4e28140"/&gt;
              &lt;mdel&gt; &lt;/mdel&gt; &lt;sga-add place="intralinear"
              sID="c57-0150__main__d4e28147"/&gt;n &lt;sga-add
              eID="c57-0150__main__d4e28147"/&gt;&lt;mod eID="c57-0150__main__d4e28140"/&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['time;']">
          <rdg wit="f1818">time;</rdg>
          <rdg wit="f1823">time;</rdg>
          <rdg wit="fThomas">time;</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['but', 'my', 'thoughts', 'rambled', 'to', 'various', 'subjects,', 'reflecting']">
          <rdg wit="f1818">but my thoughts rambled to various subjects, reflecting</rdg>
          <rdg wit="f1823">but my thoughts rambled to various subjects, reflecting</rdg>
          <rdg wit="fThomas">but my thoughts rambled to various subjects, reflecting</rdg>
          <rdg wit="f1831">but my thoughts rambled to various subjects, reflecting</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['on']">
          <rdg wit="f1818">on</rdg>
          <rdg wit="f1823">on</rdg>
          <rdg wit="fThomas">on</rdg>
      </rdgGrp>
      <rdgGrp n="['confusedly', 'on']">
          <rdg wit="f1831">confusedly on</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['possible', 'speed.']">
          <rdg wit="f1818">possible speed. </rdg>
          <rdg wit="f1823">possible speed. </rdg>
          <rdg wit="fThomas">possible speed. </rdg>
          <rdg wit="f1831">possible speed. </rdg>
          <rdg wit="fMS">&lt;sga-add eID="c57-0151__main__d4e28213"/&gt;&lt;mod
              eID="c57-0151__main__d4e28208"/&gt;possible speed.</rdg>
      </rdgGrp>
  </app>
  
  <app>
      <rdgGrp n="['&lt;p-end/&gt;', '&lt;p-start/&gt;']">
          <rdg wit="f1818">&lt;p eID="novel1_letter4_chapter22_div4_div24_p13"/&gt; &lt;p
              sID="novel1_letter4_chapter22_div4_div24_p14"/&gt;</rdg>
          <rdg wit="f1823">&lt;p eID="novel1_letter4_chapter22_div4_div23_p13"/&gt; &lt;p
              sID="novel1_letter4_chapter22_div4_div23_p14"/&gt;</rdg>
          <rdg wit="fThomas">&lt;p eID="novel1_letter4_chapter22_div4_div24_p12"/&gt; &lt;p
              sID="novel1_letter4_chapter22_div4_div24_p13"/&gt;</rdg>
          <rdg wit="f1831">&lt;p eID="novel1_letter4_chapter23_div4_div23_p13"/&gt; &lt;p
              sID="novel1_letter4_chapter23_div4_div23_p14"/&gt;</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['however,']">
          <rdg wit="f1818">However,</rdg>
          <rdg wit="f1823">However,</rdg>
          <rdg wit="fThomas">However,</rdg>
          <rdg wit="f1831">However,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['it', 'was']">
          <rdg wit="f1818">it was</rdg>
          <rdg wit="f1823">it was</rdg>
          <rdg wit="fThomas">it was</rdg>
          <rdg wit="f1831">it was</rdg>
          <rdg wit="fMS">It was</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['a']">
          <rdg wit="f1818">a</rdg>
          <rdg wit="f1823">a</rdg>
          <rdg wit="fThomas">a</rdg>
          <rdg wit="f1831">a</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['great', 'and', 'sudden']">
          <rdg wit="f1818">great and sudden</rdg>
          <rdg wit="f1823">great and sudden</rdg>
          <rdg wit="fThomas">great and sudden</rdg>
          <rdg wit="f1831">great and sudden</rdg>
          <rdg wit="fMS">great &amp; sudden</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['a']">
          <rdg wit="f1818">a</rdg>
          <rdg wit="f1823">a</rdg>
          <rdg wit="fThomas">a</rdg>
          <rdg wit="f1831">a</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['few']">
          <rdg wit="f1818">few</rdg>
          <rdg wit="f1823">few</rdg>
          <rdg wit="fThomas">few</rdg>
          <rdg wit="f1831">few</rdg>
          <rdg wit="fMS">few</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['delight', '–', 'his', 'neice']">
          <rdg wit="fMS">delight – his neice</rdg>
      </rdgGrp>
      <rdgGrp n="['their', 'delight—his']">
          <rdg wit="f1818">their delight—his</rdg>
          <rdg wit="f1823">their delight—his</rdg>
          <rdg wit="fThomas">their delight—his</rdg>
          <rdg wit="f1831">their delight—his</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['elizabeth,']">
          <rdg wit="f1831">Elizabeth,</rdg>
      </rdgGrp>
      <rdgGrp n="['niece,']">
          <rdg wit="f1818">niece,</rdg>
          <rdg wit="f1823">niece,</rdg>
          <rdg wit="fThomas">niece,</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['a', 'man']">
          <rdg wit="f1818">a man</rdg>
          <rdg wit="f1823">a man</rdg>
          <rdg wit="fThomas">a man</rdg>
          <rdg wit="f1831">a man</rdg>
          <rdg wit="fMS">a man</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['feels,']">
          <rdg wit="f1818">feels,</rdg>
          <rdg wit="f1823">feels,</rdg>
          <rdg wit="fThomas">feels,</rdg>
          <rdg wit="f1831">feels,</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['an']">
          <rdg wit="f1818">an</rdg>
          <rdg wit="f1823">an</rdg>
          <rdg wit="fThomas">an</rdg>
          <rdg wit="fMS">An</rdg>
      </rdgGrp>
      <rdgGrp n="['the', 'springs', 'of', 'existence', 'suddenly', 'gave', 'way:', 'he']">
          <rdg wit="f1831">the springs of existence suddenly gave way: he</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['apoplectic']">
          <rdg wit="f1818">apoplectic</rdg>
          <rdg wit="f1823">apoplectic</rdg>
          <rdg wit="fThomas">apoplectic</rdg>
      </rdgGrp>
      <rdgGrp n="['applapetic']">
          <rdg wit="fMS">applapetic</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['fit']">
          <rdg wit="f1818">fit</rdg>
          <rdg wit="f1823">fit</rdg>
          <rdg wit="fThomas">fit</rdg>
          <rdg wit="fMS">fit</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['brought']">
          <rdg wit="f1818">brought</rdg>
          <rdg wit="f1823">brought</rdg>
          <rdg wit="fThomas">brought</rdg>
          <rdg wit="fMS">&lt;lb n="c57-0152__main__34"/&gt;brought</rdg>
      </rdgGrp>
      <rdgGrp n="['unable', 'to', 'rise', 'from', 'his', 'bed,']">
          <rdg wit="f1831">unable to rise from his bed,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['on']">
          <rdg wit="fMS">on</rdg>
      </rdgGrp>
      <rdgGrp n="['on,']">
          <rdg wit="f1818">on,</rdg>
          <rdg wit="f1823">on,</rdg>
          <rdg wit="fThomas">on,</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['but']">
          <rdg wit="f1818">but</rdg>
          <rdg wit="f1823">but</rdg>
          <rdg wit="fThomas">but</rdg>
          <rdg wit="f1831">but</rdg>
          <rdg wit="fMS">But</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['i']">
          <rdg wit="f1823">I</rdg>
          <rdg wit="f1831">I</rdg>
          <rdg wit="fMS">I</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['you,&#34;', 'replied']">
          <rdg wit="f1818">you,” replied</rdg>
          <rdg wit="f1823">you,” replied</rdg>
          <rdg wit="fThomas">you,” replied</rdg>
          <rdg wit="f1831">you,” replied</rdg>
      </rdgGrp>
      <rdgGrp n="['you,', 'i', '', 'replied,', 'listen', 'therefore']">
          <rdg wit="fMS">you, &lt;sga-add place="intralinear" sID="c57-0154__main__d4e28883"/&gt;I
              &lt;sga-add eID="c57-0154__main__d4e28883"/&gt; replied, listen therefore</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['i,']">
          <rdg wit="f1823">I,</rdg>
      </rdgGrp>
      <rdgGrp n="['i;']">
          <rdg wit="f1818">I;</rdg>
          <rdg wit="fThomas">I;</rdg>
          <rdg wit="f1831">I;</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&#34;listen,', 'therefore,']">
          <rdg wit="f1818">“listen, therefore,</rdg>
          <rdg wit="f1823">“listen, therefore,</rdg>
          <rdg wit="fThomas">“listen, therefore,</rdg>
          <rdg wit="f1831">“listen, therefore,</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['that', 'i']">
          <rdg wit="f1818">that I</rdg>
          <rdg wit="f1823">that I</rdg>
          <rdg wit="fThomas">that I</rdg>
          <rdg wit="f1831">that I</rdg>
          <rdg wit="fMS">that I</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['should']">
          <rdg wit="f1818">should</rdg>
          <rdg wit="f1823">should</rdg>
          <rdg wit="fThomas">should</rdg>
          <rdg wit="f1831">should</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['marking']">
          <rdg wit="f1818">marking</rdg>
          <rdg wit="f1823">marking</rdg>
          <rdg wit="fThomas">marking</rdg>
          <rdg wit="f1831">marking</rdg>
          <rdg wit="fMS">marking</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['the']">
          <rdg wit="f1818">the</rdg>
          <rdg wit="f1823">the</rdg>
          <rdg wit="fThomas">the</rdg>
          <rdg wit="f1831">the</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['and', 'never', 'deviating', 'into', 'invective', 'or', 'exclamation.']">
          <rdg wit="f1818">and never deviating into invective or exclamation.</rdg>
          <rdg wit="f1823">and never deviating into invective or exclamation.</rdg>
          <rdg wit="fThomas">and never deviating into invective or exclamation.</rdg>
          <rdg wit="f1831">and never deviating into invective or exclamation.</rdg>
          <rdg wit="fMS">&lt;lb n="c57-0154__main__20"/&gt;and never deviating into invective or
              &lt;lb n="c57-0154__main__21"/&gt;exclamation.</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&lt;p-end/&gt;', '&lt;p-start/&gt;']">
          <rdg wit="f1818">&lt;p eID="novel1_letter4_chapter22_div4_div24_p21"/&gt; &lt;p
              sID="novel1_letter4_chapter22_div4_div24_p22"/&gt;</rdg>
          <rdg wit="f1823">&lt;p eID="novel1_letter4_chapter22_div4_div23_p21"/&gt; &lt;p
              sID="novel1_letter4_chapter22_div4_div23_p22"/&gt;</rdg>
          <rdg wit="fThomas">&lt;p eID="novel1_letter4_chapter22_div4_div24_p20"/&gt; &lt;p
              sID="novel1_letter4_chapter22_div4_div24_p21"/&gt;</rdg>
          <rdg wit="f1831">&lt;p eID="novel1_letter4_chapter23_div4_div23_p21"/&gt; &lt;p
              sID="novel1_letter4_chapter23_div4_div23_p22"/&gt;</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['was', 'painted', 'on', 'his', 'countenance.']">
          <rdg wit="f1818">was painted on his countenance.</rdg>
          <rdg wit="f1823">was painted on his countenance.</rdg>
          <rdg wit="fThomas">was painted on his countenance.</rdg>
          <rdg wit="f1831">was painted on his countenance.</rdg>
          <rdg wit="fMS">was painted &lt;lb n="c57-0154__main__27"/&gt;on his countenance.</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&lt;p-end/&gt;']">
          <rdg wit="f1818">&lt;p eID="novel1_letter4_chapter22_div4_div24_p22"/&gt;</rdg>
          <rdg wit="f1823">&lt;p eID="novel1_letter4_chapter22_div4_div23_p22"/&gt;</rdg>
          <rdg wit="fThomas">&lt;p eID="novel1_letter4_chapter22_div4_div24_p21"/&gt;</rdg>
          <rdg wit="f1831">&lt;p eID="novel1_letter4_chapter23_div4_div23_p22"/&gt;</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['']">
          <rdg wit="f1818">&lt;pb xml:id="F1818_v3_134" n="130"/&gt;</rdg>
          <rdg wit="f1823">&lt;pb xml:id="F1823_v2_491" n="218"/&gt;</rdg>
          <rdg wit="fThomas">&lt;pb xml:id="F1818_v3_134" n="130"/&gt;</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&lt;p-start/&gt;']">
          <rdg wit="f1818">&lt;p sID="novel1_letter4_chapter22_div4_div24_p23"/&gt;</rdg>
          <rdg wit="f1823">&lt;p sID="novel1_letter4_chapter22_div4_div23_p23"/&gt;</rdg>
          <rdg wit="fThomas">&lt;p sID="novel1_letter4_chapter22_div4_div24_p22"/&gt;</rdg>
          <rdg wit="f1831">&lt;p sID="novel1_letter4_chapter23_div4_div23_p23"/&gt;</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['and', 'i', 'believe', 'and', 'hope']">
          <rdg wit="f1818">and I believe and hope</rdg>
          <rdg wit="f1823">and I believe and hope</rdg>
          <rdg wit="fThomas">and I believe and hope</rdg>
          <rdg wit="f1831">and I believe and hope</rdg>
          <rdg wit="fMS">and &lt;lb n="c57-0154__main__33"/&gt;I believe &amp; hope</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['that']">
          <rdg wit="f1818">that</rdg>
          <rdg wit="f1823">that</rdg>
          <rdg wit="fThomas">that</rdg>
          <rdg wit="f1831">that</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['of', 'my']">
          <rdg wit="f1818">of my</rdg>
          <rdg wit="f1823">of my</rdg>
          <rdg wit="fThomas">of my</rdg>
          <rdg wit="f1831">of my</rdg>
          <rdg wit="fMS">of my</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['auditor']">
          <rdg wit="fMS">auditor</rdg>
      </rdgGrp>
      <rdgGrp n="['own']">
          <rdg wit="f1831">own</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['auditor.']">
          <rdg wit="f1818">auditor.</rdg>
          <rdg wit="f1823">auditor.</rdg>
          <rdg wit="fThomas">auditor.</rdg>
          <rdg wit="f1831">auditor.</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['intimidated', 'you']">
          <rdg wit="fMS">intimidated &lt;lb n="c57-0155__main__35"/&gt;You</rdg>
      </rdgGrp>
      <rdgGrp n="['intimidated:']">
          <rdg wit="f1823">intimidated:</rdg>
      </rdgGrp>
      <rdgGrp n="['intimidated:—&#34;you']">
          <rdg wit="f1831">intimidated:—“You</rdg>
      </rdgGrp>
      <rdgGrp n="['intimidated;']">
          <rdg wit="f1818">intimidated;</rdg>
          <rdg wit="fThomas">intimidated;</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&#34;you']">
          <rdg wit="f1818">“You</rdg>
          <rdg wit="f1823">“You</rdg>
          <rdg wit="fThomas">“You</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['angry']">
          <rdg wit="f1818">angry</rdg>
          <rdg wit="f1823">angry</rdg>
          <rdg wit="fThomas">angry</rdg>
          <rdg wit="f1831">angry</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['and']">
          <rdg wit="f1818">and</rdg>
          <rdg wit="f1823">and</rdg>
          <rdg wit="fThomas">and</rdg>
          <rdg wit="f1831">and</rdg>
          <rdg wit="fMS">&amp;</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['angry', 'and disturbed']">
          <rdg wit="fMS">angry &amp;&lt;lb n="c57-0156__main__37"/&gt;disturbed</rdg>
      </rdgGrp>
      <rdgGrp n="['disturbed,', 'and']">
          <rdg wit="f1818">disturbed, and</rdg>
          <rdg wit="f1823">disturbed, and</rdg>
          <rdg wit="fThomas">disturbed, and</rdg>
          <rdg wit="f1831">disturbed, and</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['some', 'other', 'mode', 'of', 'action.']">
          <rdg wit="f1818">some other mode of action.</rdg>
          <rdg wit="f1823">some other mode of action.</rdg>
          <rdg wit="fThomas">some other mode of action.</rdg>
          <rdg wit="f1831">some other mode of action.</rdg>
          <rdg wit="fMS">some other mode &lt;lb n="c57-0156__main__38"/&gt;of action.</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&lt;p-end/&gt;', '']">
          <rdg wit="f1818">&lt;p eID="novel1_letter4_chapter22_div4_div24_p30"/&gt; &lt;milestone
              unit="chapter" type="end" n="22"/&gt;</rdg>
          <rdg wit="f1823">&lt;p eID="novel1_letter4_chapter22_div4_div23_p30"/&gt; &lt;milestone
              unit="chapter" type="end" n="22"/&gt;</rdg>
          <rdg wit="fThomas">&lt;p eID="novel1_letter4_chapter22_div4_div24_p29"/&gt;
              &lt;milestone unit="chapter" type="end" n="22"/&gt;</rdg>
          <rdg wit="f1831">&lt;p eID="novel1_letter4_chapter23_div4_div23_p30"/&gt; &lt;milestone
              unit="chapter" type="end" n="23"/&gt;</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['bosom', '–shot–']">
          <rdg wit="fMS">bosom –shot–</rdg>
      </rdgGrp>
      <rdgGrp n="['bosom,']">
          <rdg wit="f1818">bosom,</rdg>
          <rdg wit="f1823">bosom,</rdg>
          <rdg wit="fThomas">bosom,</rdg>
          <rdg wit="f1831">bosom,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&lt;del&gt;shot&lt;/del&gt;', 'fiered', ';']">
          <rdg wit="fThomas">&lt;del rend="strikethrough"&gt;shot&lt;/del&gt; &lt;add
              place="margin" medium="pencil"&gt;fiered&lt;/add&gt; ;</rdg>
      </rdgGrp>
      <rdgGrp n="['fired;']">
          <rdg wit="f1831">fired;</rdg>
      </rdgGrp>
      <rdgGrp n="['shot;']">
          <rdg wit="f1818">shot;</rdg>
          <rdg wit="f1823">shot;</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['atten', 'tion and', 'kindness', '–', 'be']">
          <rdg wit="fMS">&lt;w ana="start"/&gt;at&lt;lb n="c57-0154__main__3"/&gt;&lt;sga-add
              place="intralinear" sID="c57-0154__main__d4e28857"/&gt;ten &lt;sga-add
              eID="c57-0154__main__d4e28857"/&gt;tion&lt;w ana="end"/&gt;&amp; kindness – Be</rdg>
      </rdgGrp>
      <rdgGrp n="['attention', 'and']">
          <rdg wit="f1818">attention and</rdg>
          <rdg wit="f1823">attention and</rdg>
          <rdg wit="fThomas">attention and</rdg>
          <rdg wit="f1831">attention and</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['kindness:', '&#34;be']">
          <rdg wit="f1818">kindness: “Be</rdg>
          <rdg wit="f1823">kindness: “Be</rdg>
          <rdg wit="fThomas">kindness: “Be</rdg>
      </rdgGrp>
      <rdgGrp n="['kindness:—&#34;be']">
          <rdg wit="f1831">kindness:—“Be</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['and']">
          <rdg wit="f1818">and</rdg>
          <rdg wit="f1823">and</rdg>
          <rdg wit="fThomas">and</rdg>
          <rdg wit="f1831">and</rdg>
          <rdg wit="fMS">&amp;&lt;mod sID="c57-0154__main__d4e28960"/&gt;&lt;sga-add
              place="sublinear" sID="c57-0154__main__d4e28962"/&gt;</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['']">
          <rdg wit="fMS">&lt;metamark function="insert"&gt;^&lt;/metamark&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['for', 'an', 'interval']">
          <rdg wit="f1823">for an interval</rdg>
          <rdg wit="f1831">for an interval</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['provisionally']">
          <rdg wit="f1818">provisionally</rdg>
          <rdg wit="fThomas">provisionally</rdg>
          <rdg wit="fMS">&lt;sga-add eID="c57-0154__main__d4e28962"/&gt;&lt;sga-add hand="#pbs"
              place="superlinear" sID="c57-0154__main__d4e28968"/&gt;provisionally</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['you', 'should']">
          <rdg wit="f1818">you should</rdg>
          <rdg wit="f1823">you should</rdg>
          <rdg wit="fThomas">you should</rdg>
          <rdg wit="f1831">you should</rdg>
          <rdg wit="fMS">you should</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['endeavour', 'to']">
          <rdg wit="f1818">endeavour to</rdg>
          <rdg wit="fThomas">endeavour to</rdg>
          <rdg wit="fMS">&lt;lb n="c57-0156__main__6"/&gt;endeavour to</rdg>
      </rdgGrp>
  </app>
  ```

