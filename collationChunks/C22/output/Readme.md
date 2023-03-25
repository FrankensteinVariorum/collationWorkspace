# 3-25-2023

- Establishing the branch, the complete files, and the readme. Running shell script here for the first time.
- [ ] MS: `have` is written as `ha ve`. Can't remember if `<sga>` code prevents this from being fixable or not.
- [ ] **Confusion::** MS has `in`, but every other version has `that had broken`. Those two statements align, and the next passages appear to be aligned. See below for reference:
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

- [ ] **Possible misalignment:** one app has `arch` and `arch-fiend,` in the same reading group, but everything except 1831 has `arch` and `fiend` in separate apps. May need to fix with longTokens, see code below for reference:
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