# Welcome to the collationWorkspace for the Frankenstein Variorum Project!

## Quick Links

* **[Python installation instructions](#installations-needed)**
* **[Collatex installation instructions](#collatex-installation-instructions)**
* **[Collation instructions](#how-to-collate-your-chunk)**

We're glad you're here to help the project and see how collation works! You're helping us with collating five versions of the novel *Frankenstein: or The Modern Prometheus* by Mary Wollstonecraft Godwin Shelley. Computationally-assisted collation involves running programs that help mark moments when different versions of a text run the same together and when they diverge from each other. Our collation process produces data about these moments and outputs them in XML that we use to build our Variorum edition of the novel, designed to show "hotspots" of change as you read each version. We are collating five versions of this novel: 

1. Manuscript notebooks written in 1816
2. 1818 first printed edition (published anonymously)
3. Thomas edition (a copy of the printed 1818 edition in which Mary Shelley and possibly others handwrote notes, marked passages to delete, and wrote in passages to add to a possible new edition of the novel. When she traveled back to England after the death of her husband, Mary Shelley left this marked copy of the novel in Italy with a friend, "Mrs. Thomas", who was remaining there--so that is why this is called the Thomas copy. We do not know its exact dates--when the markings were made on the print edition. But we know it was sometime in 1818 or after and sometime before 1824. 
4. 1823 printed edition: prepared by Mary Shelley's father William Godwin. This edition lightly edits but seems not to change the content very much from 1818. This is the first edition to publish Mary Shelley's name as the author.
5. 1831 printed edition: This is a heavily revised version of the novel, with revisions by Mary Shelley but without access to the Thomas copy. 

## Installations needed

Before you can begin collating, we need to verify that you have the following installed on your computer:

* A version of Python 3. 
    * To see if you have python installed and which version, type this in your Git Bash shell (Windows) or Terminal (Mac):
     
          python --version
          
     If you think you have multiple versions of python installed, try 
      
           which -a python
           
* If you do not have Python installed on your system, or if the version number is 2 (as in 2.7), then you need to install Python 3. 
* If you need to install Python 3, here is some guidance for Windows, Mac, and Linux operating systems: 


Visit the Python website at https://www.python.org/ and look for the **latest Stable Release for your operating system** at
https://www.python.org/downloads/

### Windows Users:

Follow steps 1 - 4 on this site, and (IMPORTANT!) **make sure you add Python 3 to your PATH variable!** : https://www.tomshardware.com/how-to/install-python-on-windows-10-and-11 . (You don't need to go on and install Mu, etc. Adding Python to your PATH should mean this is the version of Python that will engage when you run our scripts, and it will also make it easier to access in software when you need to write Python yourself.)
_Just in case we need them_, here are super detailed instructions from Python 
because Windows can be complicated: https://docs.python.org/3/using/windows.html

### Mac Users:

Super informative instructions here: https://www.dataquest.io/blog/installing-python-on-mac/.
Download the latest stable version here: https://www.python.org/downloads/macos/Links to an external site.

### Linux Users? 
Let me know if you use Linux and we'll find some guidance if you need it!

*****

## CollateX installation instructions

For this section, we are distilling this helpful but slightly dated guide: https://github.com/DiXiT-eu/collatex-tutorial/blob/master/unit1/Installation.ipynb 
 To install collateX and its dependencies, we'll use the **pip** Python package manager.

* First find out if you have pip on your computer. In your Bash shell or terminal, enter:
`pip -V`
     * If you see pip version information, you're ready to install stuff--go on to the next step. 
     * If you see an error or nothing, we'll need to install Pip. Here are instructions: 
          * **Windows**: https://phoenixnap.com/kb/install-pip-windows
          * **Mac**: https://phoenixnap.com/kb/install-pip-mac
          * **Linux**: https://www.educative.io/answers/installing-pip3-in-ubuntu
          
* With pip ready, navigate in your shell to our GitHub repo and step into the python-collation folder.
You would be going here on your computer `cd your/filepath/down/to/collationWorkspace/python-collation`
(We are not really sure this is necessary, but we have collateX here on file, so in case it's helpful let's go here for this part.)

Enter: `pip install collatex`

* Next we'll install Levenshtein, which collatex uses to measure differences between strings as it is collating documents. 
**Be careful with the spelling of this**
`pip install python-levenshtein`

That *should* be everything we need to begin, but be alert to errors in your shell as we proceed, alert us, and we will update these instructions as we go.
*****

## How to collate your "chunk"

### Getting to know your "chunk"
You will be assigned a collation unit (or units) to help with collating. These units are commonly known as "chunks" and they are numbered from 1 to 33. Each "chunk" represents a unit about the size of a chapter in the novel. Usually "chunks" are chapters, but sometimes they are parts of chapters in the novel. Most importantly, each "chunk" is a passage in which *the very beginning* and *the very end* are close to the same across all five versions of the novel. So we know that each "chunk" starts and ends in very much the same way. 

Here is the process:
* BEFORE YOU START WORK on collating a chunk: **check out a branch** using an identifier for you (like your initials) and the Collation Unit you are working on. Example: 

```
git checkout -b yxj-C25
```

You will need to push your branch to the remote repo. You can do that with:

```
git push -u origin yxj-C25
```
Or simply use `git push` and follow the instructions in your shell to push the branch. 
 

* We run our programming scripts to compare the five versions of the novel one "chunk" at a time. 
     * In your Bash shell (Windows) or Terminal (Mac), at the collationWorkspace outermost directory, run this command to activate the shell script that activates the collation processing:

     ```
     ./coll.sh
     ``` 
     This shell script will ask you some input questions: Which collation unit(s) are you processing? When you answer them it should run, show you a view of the collation processing in action, and output some files. It will be running a Python script first, followed by an XSLT script. 

     * Our Python script *tokenizes* the five input edition files, basically on words or words with punctuation marks attached. It provides normalizing information to show that strings like `&` mean the same thing as the word `and` and to help us identify meaningful XML markup that should be compared across the texts.
     * Our XSLT script then begins running to "tidy up" some common problems in the Python output. 
     * The output files come out in two stages: a "partway" file (the Python output) and a "complete" file (the XSLT output) as described next.

* We need to review the output carefully. The output will be stored in a folder named `output/` inside your assigned collation unit, and it will consist of two files named like this example for Collation unit 1:
     1. Collation_C01-partway.xml  (This is the output of our Python collation script.) 
     2. Collation_C01-complete.xml (This is an improvement on the python output made with XSLT.)
When you run the coll.sh file, it will output both of these in sequence. 
**Expect to wait a few minutes, or several minutes for the script to complete.** 

The "complete" version is completely processed with some automatic adjustments made with XSLT. We want to keep the partway version in case we need to inspect it, but usually we will not need to refer to it. 
The complete Collation output file is a single XML file showing segments in `<app>` elements where passages compare and diverge. 

* We study the output carefully and notice **misalignments**. These are problems where some words or phrases do not belong in the same comparison unit.
     * We now try to identify what causes the misalignment. (You may need some help with this at first!)
     * **Important! We do NOT edit the output file!** This is brittle and can introduce terrible errors! 
     * Instead we will add some simple markup to the input files to control their tokenization.
     
* **Now we move to correct for misalignments.** We identify passages in the source edition files to wrap in a special `<longToken>` element.
     * Ideally, we do not have to add this `<longToken>` to every file! 
     * Try to identify a location in one edition, where inserting the longToken alters the alignment. 
     * Most often we insert the `<longToken>` in the 1831 edition or the msColl edition.
     * You will learn your way with adjusting alignments by trial and error.
     * **When you begin** your collation, you should open the **msColl** edition and look for chapter headings to wrap in a `<longToken>`. 
     
* Re-run the collation script and this will generate new output files. (If you want to keep the old files around, add something to their filenames so they are not overwitten.) 

* Inspect the output again to see the effects of your insertion of a `<longToken>`. 

You may be confused at first by this process. Keep trying, adjust the position of the `<longToken>` and try your best to improve the alignment by strategically positioning these. 

When you would like the rest of the team to review your work, please open a Pull Request on this repo, and assign to @ebeshero for review. We will review and discuss issues with your alignments during weekly project meetings. 
     




    
       

