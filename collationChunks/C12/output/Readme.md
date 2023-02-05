# C12

Notice: Press the `Format and Indent` button

## Misalignments


- [x] Done by @ebeshero  From 2436 to 2464

Two words `for` and `the ` are joint in the first `<app>`. 

We might need to add a space before `<lb>` to separate words before and after `<lb>`.

```xml
<app>
		<rdgGrp n="['for']">
			<rdg wit="f1818">for</rdg>
			<rdg wit="f1823">for</rdg>
			<rdg wit="fThomas">for</rdg>
			<rdg wit="f1831">for</rdg>
		</rdgGrp>
		<rdgGrp n="['forthe', 'minutiæ']">
			<rdg wit="fMS">for&lt;lb n="c56-0069__main__1"/&gt;the minutiæ</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['natural', 'science;']">
			<rdg wit="f1831">natural science;</rdg>
		</rdgGrp>
		<rdgGrp n="['the', 'minutæ']">
			<rdg wit="f1818">the minutæ</rdg>
			<rdg wit="f1823">the minutæ</rdg>
			<rdg wit="fThomas">the minutæ</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['of', 'science.']">
			<rdg wit="f1818">of science.</rdg>
			<rdg wit="f1823">of science.</rdg>
			<rdg wit="fThomas">of science.</rdg>
			<rdg wit="fMS">of science.</rdg>
		</rdgGrp>
	</app>
```

- [x] REVISED by @ebeshero : improved alignment for these next two: 
From 2567 to 2588

`persian` and `arabic` for `FMS` in the first `<app>` should go down.

```xml
<app>
		<rdgGrp n="['to', 'geneva.']">
			<rdg wit="f1818">to Geneva.</rdg>
			<rdg wit="f1823">to Geneva.</rdg>
			<rdg wit="fThomas">to Geneva.</rdg>
		</rdgGrp>
		<rdgGrp
			n="['–', '&lt;delstart/&gt;greek&lt;delend/&gt;', 'persian', '', '&lt;delstart/&gt;and&lt;delend/&gt;', 'arabic']">
			<rdg wit="fMS">– &lt;del rend="strikethrough"
				xml:id="c56-0069__main__d5e14244"&gt;Greek&lt;/del&gt; Persian &lt;lb
				n="c56-0069__main__5"/&gt; &lt;del rend="strikethrough"
				xml:id="c56-0069__main__d5e14249"&gt;&amp;&lt;/del&gt; Arabic</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['persian,', 'arabic,']">
			<rdg wit="f1818">Persian, Arabic,</rdg>
			<rdg wit="f1823">Persian, Arabic,</rdg>
			<rdg wit="fThomas">Persian, Arabic,</rdg>
			<rdg wit="f1831">Persian, Arabic,</rdg>
		</rdgGrp>
	</app>
```

* From 2598 to 2618

`engaged` should go down.

```xml
<app>
	<rdgGrp n="['hebrew']">
		<rdg wit="fMS">Hebrew</rdg>
	</rdgGrp>
	<rdgGrp n="['hebrew,']">
		<rdg wit="f1818">Hebrew,</rdg>
		<rdg wit="f1823">Hebrew,</rdg>
		<rdg wit="fThomas">Hebrew,</rdg>
	</rdgGrp>
	<rdgGrp n="['sanscrit', 'languages', 'engaged']">
		<rdg wit="f1831">Sanscrit languages engaged</rdg>
	</rdgGrp>
</app>
<app>
	<rdgGrp n="['gained']">
		<rdg wit="f1818">gained</rdg>
		<rdg wit="f1823">gained</rdg>
		<rdg wit="fThomas">gained</rdg>
		<rdg wit="fMS">gained</rdg>
	</rdgGrp>
</app>
```