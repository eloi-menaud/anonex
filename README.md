# anonex
regex-based file editing tool, for annunciation and more

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
echo 'alias anonex="Python3 -B path/to/anonex.py"' >> ~/.zshrc
source ~/.zshrc
```
- test readiness :
```bash
anonex --help
```

# How it works

## conf file
> to make it easier to use, all configuration with regex is done via a conf file instead of a command line.

first create a configuration file named `anonex.conf` and add this :
```ini
[DEFAULT]
file=path/to/fil
inex=regex for selection
outex=rgex for overwrite rules
```
exemple:

```ini
# anonex.conf
[DEFAULT]
file=dump.txt
inex=[a-z]+@gmail.com
outex=[a-z]{5}@[a-z]{3}.com
```
```ini
# dump.txt
eloi@gmail.com
pierre@gmail.com
antoine@gmail.com
```

##  inex
this is the regex that will be used to match the expressions. "I want to replace all the patterns that look like **inex** to edit them".

this is just regex

##  outex
these are transformation rules in the form of inverse reggex. "i want to transform into something that looks like outex".

for exemple, in the previus exmple `[a-z]{5}@[a-z]{3}.com` will generate random email with 5 letter before @ and a domain name with 3 letter.

2- relation with groups

but its much more powerful, cause you can do small relation :
if you have an ligne like
```
eloi menaud : eloi.menaud@gmail.com
```
and you want to anonimise it, you won't something like,
```
joe smith : michael.dias@gmail.com
```
but something like,
```
joe smith : joe.smith@gmail.com
```

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
