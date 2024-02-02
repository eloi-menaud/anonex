# anonex
regex-based file editing tool, for anonymisation and more

# Get started
### prerequis
- have [python3](https://www.python.org/downloads/)
- have [pip3](https://www.educative.io/answers/installing-pip3-in-ubuntu)
- install xeger :
```bash
pip3 install xeger
```

### set up
- clone the project

- create alias :

```bash
echo 'alias anonex="python3 -B path/to/anonex.py"' >> ~/.zshrc
source ~/.zshrc
```
- test readiness :
```bash
anonex --help
```

## conf file
> to make it easier to use, all configuration with regex is done via a conf file instead of a command line.

first create a configuration file named `anonex.conf` and add this :
```ini
[DEFAULT]
file=path/to/fil
inex=regex for selection
outex=rgex for overwrite rules
```

<br>
<br>

# How it works

##  inex
this is the regex that will be used to match the expressions. "I want to replace all the patterns that look like **inex** to edit them".

this is just regex

##  outex
these are transformation rules in the form of inverse reggex. "i want to transform into something that looks like outex".

for exemple, in the previus exmple `[a-z]{5}@[a-z]{3}.com` will generate random email with 5 letter before @ and a domain name with 3 letter.

2- relation with groups

for this you can use `regex groups` by doing something like :
```
([0-9])-\1 # => 1-1, 2-2, 6-6, ...

the (...) create a groupe and store it
the \1 try yo retreive the first group

([0-9])-\1
   |____|
```

3- special outex syntax :
> as some regex are difficult to create and must be at least coherent, here are some specific syntaxes

- ~ln  : last name
- ~fn  : first name
- ~ddb : date with database syntaxe yyyy-mm-dd hh:mm:ss
- ~da : date with classic americain syntaxe mm/dd/yyyy
- ~de : date with classic americain syntaxe mm/dd/yyyy

```
use like :
outex=[0-9]~ln ~dra => 7smith 02/28/2012
```
**add your own syntax** by adding fonction in the custom_syntax.py