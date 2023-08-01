- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['i', 'collected']">
          <rdg wit="f1818">I collected</rdg>
          <rdg wit="f1823">I collected</rdg>
          <rdg wit="fThomas">I collected</rdg>
          <rdg wit="f1831">I collected</rdg>
          <rdg wit="fMS">I collected</rdg>
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

- [x] merge two apps:

  ```xml
  <app>
      <rdgGrp n="['', '&lt;del&gt;disapp&lt;/del&gt;']">
          <rdg wit="fMS">&lt;lb n="c56-0048__left_margin__6"/&gt; &lt;del rend="strikethrough"
              xml:id="c56-0048__left_margin__d5e10299"&gt;disapp&lt;/del&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['disappointment;']">
          <rdg wit="f1823">disappointment;</rdg>
          <rdg wit="f1831">disappointment;</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['disappointment:']">
          <rdg wit="f1818">disappointment:</rdg>
          <rdg wit="fThomas">disappointment:</rdg>
          <rdg wit="fMS">&lt;lb n="c56-0048__left_margin__7"/&gt;disappointment:</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['dreams', 'that', 'had', 'been', 'my', 'food', 'and']">
          <rdg wit="f1818">dreams that had been my food and</rdg>
          <rdg wit="f1823">dreams that had been my food and</rdg>
          <rdg wit="fThomas">dreams that had been my food and</rdg>
          <rdg wit="f1831">dreams that had been my food and</rdg>
      </rdgGrp>
      <rdgGrp
              n="['', '&lt;del&gt;creature as i never before existed.&lt;/del&gt;', 'dreams', 'that', 'had', 'been', 'my', 'food', 'and']">
          <rdg wit="fMS">&lt;anchor xml:id="c56-0048.02"/&gt;&lt;sga-add
              eID="c56-0048__main__d5e10270"/&gt; &lt;del rend="strikethrough"
              xml:id="c56-0048__main__d5e10309"&gt;creature as I never before existed.&lt;/del&gt;
              &lt;anchor xml:id="c56-0048.04"/&gt;&lt;lb n="c56-0048__main__14"/&gt;Dreams that
              had been my food and</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['pleasant']">
          <rdg wit="f1818">pleasant</rdg>
          <rdg wit="f1823">pleasant</rdg>
          <rdg wit="fThomas">pleasant</rdg>
          <rdg wit="f1831">pleasant</rdg>
      </rdgGrp>
  </app>
  ```

- [x] misalignment:

  ```xml
  <app>
      <rdgGrp n="['by', 'the']">
          <rdg wit="f1818">by the</rdg>
          <rdg wit="f1823">by the</rdg>
          <rdg wit="fThomas">by the</rdg>
          <rdg wit="f1831">by the</rdg>
          <rdg wit="fMS">by the</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&lt;del&gt;drizzling&lt;/del&gt;']">
          <rdg wit="fMS">&lt;del rend="strikethrough"
              xml:id="c56-0049__main__d5e10432"&gt;drizzling&lt;/del&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['rain,']">
          <rdg wit="f1818">rain,</rdg>
          <rdg wit="fThomas">rain,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['rain']">
          <rdg wit="f1823">rain</rdg>
          <rdg wit="f1831">rain</rdg>
          <rdg wit="fMS">rain</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['the', 'inn', 'at', 'which', 'the']">
          <rdg wit="f1818">the inn at which the </rdg>
          <rdg wit="f1823">the inn at which the </rdg>
          <rdg wit="fThomas">the inn at which the </rdg>
          <rdg wit="f1831">the inn at which the </rdg>
          <rdg wit="fMS">&lt;sga-add eID="c56-0049__main__d5e10527"/&gt;&lt;mod
              eID="c56-0049__main__d5e10522"/&gt;the Inn at which the</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['various']">
          <rdg wit="f1818">various</rdg>
          <rdg wit="f1823">various</rdg>
          <rdg wit="fThomas">various</rdg>
          <rdg wit="f1831">various</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 apps:

  ```xml
  <!-- search `knew not` to locate -->
  <app>
      <rdgGrp n="['but']">
          <rdg wit="f1818">but</rdg>
          <rdg wit="f1823">but</rdg>
          <rdg wit="fThomas">but</rdg>
          <rdg wit="f1831">but</rdg>
          <rdg wit="fMS">but</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['i']">
          <rdg wit="f1818">I</rdg>
          <rdg wit="f1823">I</rdg>
          <rdg wit="fThomas">I</rdg>
          <rdg wit="f1831">I</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['&#34;you', 'may']">
          <rdg wit="f1818">“You may</rdg>
          <rdg wit="f1823">“You may</rdg>
          <rdg wit="fThomas">“You may</rdg>
          <rdg wit="f1831">“You may</rdg>
      </rdgGrp>
      <rdgGrp n="['&lt;p-end/&gt;', '&lt;p-start/&gt;', '&#34;you', 'may']">
          <rdg wit="fMS">&lt;milestone unit="tei:p-END"/&gt; &lt;milestone unit="tei:p-START"/&gt;
              &lt;lb n="c56-0050__main__24"/&gt;"You may</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['easily']">
          <rdg wit="f1818">easily</rdg>
          <rdg wit="f1823">easily</rdg>
          <rdg wit="fThomas">easily</rdg>
          <rdg wit="f1831">easily</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['all']">
          <rdg wit="f1831">all</rdg>
      </rdgGrp>
      <rdgGrp n="['it']">
          <rdg wit="f1818">it</rdg>
          <rdg wit="f1823">it</rdg>
          <rdg wit="fThomas">it</rdg>
          <rdg wit="fMS">it</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['is']">
          <rdg wit="fMS">is</rdg>
      </rdgGrp>
      <rdgGrp n="['was']">
          <rdg wit="f1818">was</rdg>
          <rdg wit="f1823">was</rdg>
          <rdg wit="fThomas">was</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['not', 'absolutely']">
          <rdg wit="f1818">not absolutely</rdg>
          <rdg wit="f1823">not absolutely</rdg>
          <rdg wit="fThomas">not absolutely</rdg>
          <rdg wit="fMS">not absolutely</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['not']">
          <rdg wit="f1818">not</rdg>
          <rdg wit="f1823">not</rdg>
          <rdg wit="fThomas">not</rdg>
          <rdg wit="f1831">not</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['comprised', 'in', 'the', 'noble', 'art', 'of']">
          <rdg wit="f1831">comprised in the noble art of</rdg>
      </rdgGrp>
      <rdgGrp n="['to']">
          <rdg wit="f1818">to</rdg>
          <rdg wit="f1823">to</rdg>
          <rdg wit="fThomas">to</rdg>
          <rdg wit="fMS">to</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&#34;know', 'nothing']">
          <rdg wit="fMS">&lt;lb n="c56-0050__main__29"/&gt;"know nothing</rdg>
      </rdgGrp>
      <rdgGrp n="['understand', 'any', 'thing']">
          <rdg wit="f1818">understand any thing</rdg>
          <rdg wit="f1823">understand any thing</rdg>
          <rdg wit="fThomas">understand any thing</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['except']">
          <rdg wit="f1818">except</rdg>
          <rdg wit="f1823">except</rdg>
          <rdg wit="fThomas">except</rdg>
          <rdg wit="fMS">except</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['and', 'he']">
          <rdg wit="f1818">and he</rdg>
          <rdg wit="f1823">and he</rdg>
          <rdg wit="fThomas">and he</rdg>
          <rdg wit="f1831">and he</rdg>
          <rdg wit="fMS">and he</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['has']">
          <rdg wit="f1818">has</rdg>
          <rdg wit="f1823">has</rdg>
          <rdg wit="fThomas">has</rdg>
          <rdg wit="f1831">has</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['have', 'lately', 'been', 'so']">
          <rdg wit="f1818">have lately been so</rdg>
          <rdg wit="f1823">have lately been so</rdg>
          <rdg wit="fThomas">have lately been so</rdg>
          <rdg wit="f1831">have lately been so</rdg>
      </rdgGrp>
      <rdgGrp n="['replied', '&#34;i', 'have', 'lately', 'been', 'so']">
          <rdg wit="fMS">replied &lt;lb n="c56-0051__main__27"/&gt;"I have lately been so</rdg>
      </rdgGrp>
  </app>
  
  <app>
      <rdgGrp n="['deeply']">
          <rdg wit="f1818">deeply</rdg>
          <rdg wit="f1823">deeply</rdg>
          <rdg wit="fThomas">deeply</rdg>
          <rdg wit="f1831">deeply</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['are']">
          <rdg wit="f1818">are</rdg>
          <rdg wit="f1823">are</rdg>
          <rdg wit="fThomas">are</rdg>
          <rdg wit="f1831">are</rdg>
          <rdg wit="fMS">are</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['now']">
          <rdg wit="f1818">now</rdg>
          <rdg wit="f1823">now</rdg>
          <rdg wit="fThomas">now</rdg>
          <rdg wit="f1831">now</rdg>
      </rdgGrp>
  </app>
  ```

- [x] merge these apps:

  ```xml
  <app>
      <rdgGrp n="['still']">
          <rdg wit="f1818">still</rdg>
          <rdg wit="f1823">still</rdg>
          <rdg wit="fThomas">still</rdg>
          <rdg wit="f1831">still</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['be']">
          <rdg wit="f1818">be</rdg>
          <rdg wit="f1823">be</rdg>
          <rdg wit="fThomas">be</rdg>
          <rdg wit="f1831">be</rdg>
          <rdg wit="fMS">&lt;lb n="c56-0052__main__13"/&gt;be</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['still', 'there—alive']">
          <rdg wit="fMS">still there—alive</rdg>
      </rdgGrp>
      <rdgGrp n="['there,', 'alive,']">
          <rdg wit="f1818">there, alive,</rdg>
          <rdg wit="f1823">there, alive,</rdg>
          <rdg wit="fThomas">there, alive,</rdg>
          <rdg wit="f1831">there, alive,</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp
              n="['i', 'darted', 'up', 'towards', 'my', 'own', 'room.', 'my', 'hand', 'was', 'already', 'on', 'the', 'lock']">
          <rdg wit="f1818">I darted up towards my own room. My hand was already on the lock</rdg>
          <rdg wit="f1823">I darted up towards my own room. My hand was already on the lock</rdg>
          <rdg wit="fThomas">I darted up towards my own room. My hand was already on the
              lock</rdg>
          <rdg wit="f1831">I darted up towards my own room. My hand was already on the lock</rdg>
      </rdgGrp>
      <rdgGrp
              n="['&lt;del&gt;while&lt;/del&gt;', 'i', 'darted', 'up', 'towards', 'my', 'own', 'room.', 'my', 'hand', 'was', 'already', 'on', 'the', 'lock']">
          <rdg wit="fMS">&lt;del rend="strikethrough"
              xml:id="c56-0052__main__d5e11050"&gt;while&lt;/del&gt; I darted up towards &lt;lb
              n="c56-0052__main__20"/&gt;my own room. My hand was already &lt;lb
              n="c56-0052__main__21"/&gt;on the lock</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['of', 'the', 'door']">
          <rdg wit="f1818">of the door</rdg>
          <rdg wit="f1823">of the door</rdg>
          <rdg wit="fThomas">of the door</rdg>
          <rdg wit="f1831">of the door</rdg>
      </rdgGrp>
  </app>
  ```

  - [x] merge two apps:

    ```xml
    <app>
        <rdgGrp n="['the', 'servant']">
            <rdg wit="f1818">the servant</rdg>
            <rdg wit="f1823">the servant</rdg>
            <rdg wit="fThomas">the servant</rdg>
            <rdg wit="f1831">the servant</rdg>
        </rdgGrp>
        <rdgGrp n="['present', 'ly', 'the', 'servant']">
            <rdg wit="fMS">present &lt;lb n="c56-0053__main__7"/&gt;ly the servant</rdg>
        </rdgGrp>
    </app>
    <app>
        <rdgGrp n="['presently']">
            <rdg wit="f1818">presently</rdg>
            <rdg wit="f1823">presently</rdg>
            <rdg wit="fThomas">presently</rdg>
            <rdg wit="f1831">presently</rdg>
        </rdgGrp>
    </app>
    ```

  - [x] app with less than 5 rdgs:

    ```xml
    <app>
        <rdgGrp n="['before', 'my', 'eyes,', 'for', 'i', 'thought', 'i', 'saw', 'the']">
            <rdg wit="f1818">before my eyes, for I thought I saw the</rdg>
            <rdg wit="f1823">before my eyes, for I thought I saw the</rdg>
            <rdg wit="fThomas">before my eyes, for I thought I saw the</rdg>
            <rdg wit="f1831">before my eyes, for I thought I saw the</rdg>
            <rdg wit="fMS">before my eyes, for I thought &lt;lb n="c56-0053__main__29"/&gt;I saw
                &lt;shi rend="underline"&gt;the</rdg>
        </rdgGrp>
    </app>
    <app>
        <rdgGrp n="['dreaded']">
            <rdg wit="f1818">dreaded</rdg>
            <rdg wit="f1823">dreaded</rdg>
            <rdg wit="fThomas">dreaded</rdg>
            <rdg wit="f1831">dreaded</rdg>
        </rdgGrp>
    </app>
    ```

  - [x] app with less than 5 rdgs:

    ```xml
    <app>
        <rdgGrp n="['the']">
            <rdg wit="f1818">the</rdg>
            <rdg wit="f1823">the</rdg>
            <rdg wit="fThomas">the</rdg>
            <rdg wit="f1831">the</rdg>
        </rdgGrp>
    </app>
    <app>
        <rdgGrp n="['witness']">
            <rdg wit="f1818">witness</rdg>
            <rdg wit="f1823">witness</rdg>
            <rdg wit="fThomas">witness</rdg>
            <rdg wit="f1831">witness</rdg>
            <rdg wit="fMS">witness</rdg>
        </rdgGrp>
    </app>
    <app>
        <rdgGrp n="['of']">
            <rdg wit="f1818">of</rdg>
            <rdg wit="f1823">of</rdg>
            <rdg wit="fThomas">of</rdg>
            <rdg wit="f1831">of</rdg>
        </rdgGrp>
    </app>
    ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['he', 'at', 'first', 'believed', 'them']">
          <rdg wit="f1818">he at first believed them</rdg>
          <rdg wit="f1823">he at first believed them</rdg>
          <rdg wit="fThomas">he at first believed them</rdg>
          <rdg wit="f1831">he at first believed them</rdg>
          <rdg wit="fMS">he at first believed &lt;lb n="c56-0055__main__26"/&gt;them</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['to', 'be']">
          <rdg wit="f1818">to be</rdg>
          <rdg wit="f1823">to be</rdg>
          <rdg wit="fThomas">to be</rdg>
          <rdg wit="f1831">to be</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['disorder']">
          <rdg wit="f1818">disorder </rdg>
          <rdg wit="f1823">disorder </rdg>
          <rdg wit="fThomas">disorder </rdg>
          <rdg wit="f1831">disorder </rdg>
          <rdg wit="fMS">&lt;sga-add eID="c56-0056__main__d5e11455"/&gt;&lt;anchor
              xml:id="c56-0056.02"/&gt;&lt;lb n="c56-0056__left_margin__1"/&gt;disorder</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['indeed']">
          <rdg wit="f1818">indeed</rdg>
          <rdg wit="f1823">indeed</rdg>
          <rdg wit="fThomas">indeed</rdg>
          <rdg wit="f1831">indeed</rdg>
      </rdgGrp>
  </app>
  <app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['and', 'that']">
          <rdg wit="f1818">and that</rdg>
          <rdg wit="f1823">and that</rdg>
          <rdg wit="fThomas">and that</rdg>
          <rdg wit="f1831">and that</rdg>
          <rdg wit="fMS">and that</rdg>
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

- [x] merge these apps excluding the token `to`:

  ```xml
  <app>
      <rdgGrp n="['perhaps']">
          <rdg wit="f1818">perhaps</rdg>
          <rdg wit="f1823">perhaps</rdg>
          <rdg wit="fThomas">perhaps</rdg>
          <rdg wit="f1831">perhaps</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['be', 'glad']">
          <rdg wit="f1818">be glad</rdg>
          <rdg wit="f1823">be glad</rdg>
          <rdg wit="fThomas">be glad</rdg>
          <rdg wit="f1831">be glad</rdg>
          <rdg wit="fMS">be glad</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['perhaps', '&#34;to']">
          <rdg wit="fMS">perhaps &lt;lb n="c56-0057__Pt1__main__24"/&gt;"to</rdg>
      </rdgGrp>
      <rdgGrp n="['to']">
          <rdg wit="f1818">to</rdg>
          <rdg wit="f1823">to</rdg>
          <rdg wit="fThomas">to</rdg>
          <rdg wit="f1831">to</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['greatest', 'remorse', 'for', 'the', 'disappointment']">
          <rdg wit="f1818">greatest remorse for the disappointment</rdg>
          <rdg wit="f1823">greatest remorse for the disappointment</rdg>
          <rdg wit="fThomas">greatest remorse for the disappointment</rdg>
          <rdg wit="f1831">greatest remorse for the disappointment</rdg>
          <rdg wit="fMS">greatest remorse for the &lt;w ana="start"/&gt;disap&lt;lb
              n="c56-0056__main__25"/&gt;pointment&lt;w ana="end"/&gt;</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['of', 'which']">
          <rdg wit="f1818">of which</rdg>
          <rdg wit="f1823">of which</rdg>
          <rdg wit="fThomas">of which</rdg>
          <rdg wit="f1831">of which</rdg>
      </rdgGrp>
  </app>
  ```

- [x] merge two apps:

  ```xml
  <app>
      <rdgGrp n="['him']">
          <rdg wit="f1818">him</rdg>
          <rdg wit="f1823">him</rdg>
          <rdg wit="fThomas">him</rdg>
          <rdg wit="fMS">him</rdg>
      </rdgGrp>
      <rdgGrp n="['him,', 'therefore,']">
          <rdg wit="f1831">him, therefore,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['therefore']">
          <rdg wit="f1818">therefore</rdg>
          <rdg wit="f1823">therefore</rdg>
          <rdg wit="fThomas">therefore</rdg>
      </rdgGrp>
      <rdgGrp n="['', '', 'therefore']">
          <rdg wit="fMS">&lt;mod sID="c56-0052__main__d5e11030"/&gt;&lt;sga-add place="sublinear"
              sID="c56-0052__main__d5e11032"/&gt; &lt;metamark
              function="insert"&gt;^&lt;/metamark&gt; &lt;sga-add
              eID="c56-0052__main__d5e11032"/&gt;&lt;sga-add hand="#pbs" place="superlinear"
              sID="c56-0052__main__d5e11038"/&gt;therefore</rdg>
      </rdgGrp>
  </app>
  
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['me,']">
          <rdg wit="fMS">me,</rdg>
      </rdgGrp>
      <rdgGrp n="['me:']">
          <rdg wit="f1818">me:</rdg>
          <rdg wit="f1823">me:</rdg>
          <rdg wit="fThomas">me:</rdg>
      </rdgGrp>
      <rdgGrp n="['me:—']">
          <rdg wit="f1831">me:—</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&lt;p-end/&gt;', '&lt;p-start/&gt;', '']">
          <rdg wit="f1818">&lt;p eID="novel1_letter4_chapter4_div4_div4_p7"/&gt; &lt;p
              sID="novel1_letter4_chapter4_div4_div4_p8"/&gt; &lt;cit
              sID="novel1_letter4_chapter4_div4_div4_p8_cit1"/&gt;</rdg>
          <rdg wit="f1823">&lt;p eID="novel1_letter4_chapter4_div4_div4_p7"/&gt; &lt;p
              sID="novel1_letter4_chapter4_div4_div4_p8"/&gt; &lt;cit
              sID="novel1_letter4_chapter4_div4_div4_p8_cit1"/&gt;</rdg>
          <rdg wit="fThomas">&lt;p eID="novel1_letter4_chapter4_div4_div4_p7"/&gt; &lt;p
              sID="novel1_letter4_chapter4_div4_div4_p8"/&gt; &lt;cit
              sID="novel1_letter4_chapter4_div4_div4_p8_cit1"/&gt;</rdg>
          <rdg wit="f1831">&lt;p eID="novel1_letter4_chapter5_div4_div5_p7"/&gt; &lt;p
              sID="novel1_letter4_chapter5_div4_div5_p8"/&gt; &lt;cit
              sID="novel1_letter4_chapter5_div4_div5_p8_cit1"/&gt;</rdg>
      </rdgGrp>
  </app>
  ```
- [x] Adjusting "unable to endure" passage to help editions line up properly (not variant really)
- [ ] Adjusting "of a lustrous black" passage: ebb: We ran into problems adjusting this.
"of a lustrous black" is the same in all editions, but it's a left-margin insertion near a page-beginning in the MS edition (lots of surface, zone, and other markup makes it generate a couple of empty tokens)
We tried wrapping longTokens to try to prevent the empty tokens from appearing, but it causes a problem in the postCollation pipeline, so I'm removing the longToken here. 
We 

  