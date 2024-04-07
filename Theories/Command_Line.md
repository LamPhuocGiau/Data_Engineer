# Command Line
## Table of Contents
  - [Navigation](#Navigation)
  - [Manipulation](#Manipulation)
  - [Redirection](#Redirection)
  - [Environment](#Environment)
## Navigation

Action|Mac/Linux Command|Windows Command
---|---|---
List files/directories |	ls |	dir
Print working directory	| pwd	| chdir
Change directory |	cd |	cd
Create new directory |	mkdir |	md
Create new file	| touch	| echo "hello world" > hello.txt
Clear screen	| clear	| cls

## Manipulation

Action	|Mac/Linux Command|	Windows Command
---|---|---
View contents of an individual file	|cat	|type
Copy file or directory	|cp|	copy
Move files (without making copy)	|mv|	ren
Delete files or directories|	rm|	del

## Redirection

Action	|Mac/Linux Command	|Windows Command
---|---|---
Redirect output	|>	|>
Pipe, or transfer, output	|| |	|
Append output to another file	|>>|	>>
Search files for a pattern match|	grep	|find

## Environment

Action | Mac/Linux Command	| Windows Command
--- | --- | ---
View all environment variables	| env	| set
Set an environment variable	export | VAR=value	| setx variable value (administrator mode)
Print specific variable	| echo $VAR	| echo %VAR%
