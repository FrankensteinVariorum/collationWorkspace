# Notes

- [ ] **MS does not align here** Watch how the collation lines up around long deleted passage in Thomas:
```
<longToken>No youth could have passed more <pb xml:id="F1818_v1_061" n="049"/>happily than
  mine.</longToken> <longToken>My parents were indulgent, and my companions amiable....</longToken>
```
Recommend editing by hand.
- [x]  Watch for this longToken: how does it align?
```xml
 <longToken>fancy. I remember, when he was nine years old, he wrote a fairy tale, which was the
    delight and amazement of all his companions.</longToken>
```

- [x]  1831 "it may appear strange" doesn't line up w/ consecutive longTokens. Removing it: check what happens.

- [x]  Check "most undivided attention" / "undivided attention" passage 
* Reset 1831 longToken to go *inside* the paragraph at "Thus strangely are our souls constructed..."

- [x] Check on Chapter II / III break
- [x] Check alignment around "a respite of some weeks" (when Victor finally is off to Ingolstadat)
- [x] MS has a Chap 4! corrected alignment with "The next morning I delivered"
- [x] Corrected: Watch for 1831: "On the same day, I paid M. Waldman a visit." vs. "paid him a visit the same evening"

- [x] merge two apps: wrapping `I include Henry` with longToken in 1818, 1823, and Thomas

  ```xml
  <app>
      <rdgGrp n="['description', 'of', 'our', 'domestic', 'circle', 'i', 'include']">
          <rdg wit="f1818">description of our domestic circle I include</rdg>
          <rdg wit="f1823">description of our domestic circle I include</rdg>
          <rdg wit="fThomas">description of our domestic circle I include</rdg>
          <rdg wit="fMS">&lt;sga-add eID="c56-0012__left_margin__d5e679"/&gt;&lt;mod
              eID="c56-0012__left_margin__d5e674"/&gt;&lt;w ana="start"/&gt;descrip&lt;lb
              n="c56-0012__left_margin__2"/&gt;tion&lt;w ana="end"/&gt; of our &lt;w
              ana="start"/&gt;do&lt;lb n="c56-0012__left_margin__3"/&gt;mestic&lt;w ana="end"/&gt;
              circle &lt;lb n="c56-0012__left_margin__4"/&gt;I include</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['henry']">
          <rdg wit="f1818">Henry</rdg>
          <rdg wit="f1823">Henry</rdg>
          <rdg wit="fThomas">Henry</rdg>
      </rdgGrp>
      <rdgGrp
              n="['', '&lt;del&gt;i include&lt;/del&gt;', '', '&lt;del&gt;hen&lt;/del&gt;', 'henry']">
          <rdg wit="fMS">&lt;anchor xml:id="c56-0012.06"/&gt;&lt;sga-add
              eID="c56-0012__main__d5e657"/&gt; &lt;del rend="strikethrough"
              xml:id="c56-0012__main__d5e703"&gt;I include&lt;/del&gt; &lt;mod
              eID="c56-0012__main__d5e655"/&gt; &lt;del rend="strikethrough"
              xml:id="c56-0012__main__d5e707"&gt;Hen&lt;/del&gt; Henry</rdg>
      </rdgGrp>
  </app>
  ```

- [ ] check where `\t` after `was` comes from in MS.

  ```xml
  <rdgGrp
          n="['was\t &lt;mdel&gt;w&lt;/mdel&gt; should probably have  aplied myself to &lt;del&gt;m&lt;/del&gt; the more &lt;del&gt;ra&lt;/del&gt; rational  theory of chemistry which &lt;del&gt;has at present&lt;/del&gt; has resulted from modern discoveries    &lt;del&gt;the approbation of the learned.&lt;/del&gt;']">
      <rdg wit="fMS">&lt;longToken&gt;was &lt;mod xml:space="preserve"
          sID="c56-0006__main__d5e1294"/&gt; &lt;mdel&gt;w&lt;/mdel&gt; &lt;sga-add
          hand="#pbs" place="intralinear" sID="c56-0006__main__d5e1296"/&gt;sh&lt;sga-add
          eID="c56-0006__main__d5e1296"/&gt;&lt;mod eID="c56-0006__main__d5e1294"/&gt;ould
          probably have &lt;lb n="c56-0006__main__11"/&gt;aplied myself to &lt;del
          rend="strikethrough" xml:id="c56-0006__main__d5e1301"&gt;m&lt;/del&gt; the more
          &lt;del rend="strikethrough" xml:id="c56-0006__main__d5e1304"&gt;ra&lt;/del&gt;
          rational &lt;lb n="c56-0006__main__12"/&gt;theory of chemistry which &lt;del
          next="#c56-0006.01" rend="strikethrough" xml:id="c56-0006__main__d5e1310"&gt;has at
          present&lt;/del&gt; &lt;sga-add hand="#pbs" next="#c56-0006.02" place="superlinear"
          sID="c56-0006__main__d5e1313"/&gt;has resulted from modern discoveries &lt;sga-add
          eID="c56-0006__main__d5e1313"/&gt; &lt;lb n="c56-0006__main__13"/&gt; &lt;del
          rend="strikethrough" xml:id="c56-0006__main__d5e1318"&gt;the approbation of the
          learned.&lt;/del&gt;&lt;/longToken&gt;</rdg>
  </rdgGrp>
  ```

  Solved: `\t` is from a tab in the longToken.