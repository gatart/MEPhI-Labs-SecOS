* Что происходит при прерывании скрипта `text-trap.sh`? Объясните, почему.
```
After Ctrh+c is pressed, the process "text-trap.sh" catches signal SIGINT (Signal Interrupt) and crashes.
```

* Напишите, по какой причине выводы команды `ls -l /proc/self` и `ls -l /proc/$$` отличаются?
```
/proc/self - symbolic link which point at the current process. It means that the value of this link depends on process which calls it. `ls -l /proc/self/` returns `ls` identificator.

`ls -l /proc/$$` correspond to the current bash shell ($$ is the process ID (PID) of the current script)
```

* Напишите, какие дескрипторы в выводе команды `ls -l /proc/self/fd` отвечают за `stdin`, `stdout`, `stderr`.
```
0 - stdin 
1 - stdout
2 - stderr
```

* Что происходит с дескрипторами при перенаправлении потоков `stdout` и `stderr` в файлы при выполнении команды `ls -l /proc/self/fd > /tmp/ls.out 2> /tmp/ls.err`?
```
File descriptors are reassigned. Standart output stream redirects to file /tmp/ls.out and diagnostic stream redirects to /tmp/ls.err
```

* Запишите эту же команду, добавив к ней перенаправление потока `stdin`. Что изменилось?
```
ls -l /proc/self/fd < /tmp/ls.in > /tmp/ls.out 2> /tmp/ls.err
```
```
If /tmp/ls.in doesn't exist, the error message will send to /tmp/ls.err, otherwise the commend output will be sent to /tmp/ls.out
```

* Какой эффект наблюдается при выполнении команды `exec ps -l`?
```
The current shell process is replaced by `ps -l` command process. The output of this command goes to standart output stream and then the shell process is terminated.
```

* Что означает `pos` при выводе содержимого файла `/proc/$$/fdinfo/3`?
```
The current position of read-write pointer in the open Bash shell process file.
```

* Существует ли возможность читать содержимое файла `test.out` даже после его удаления? Почему так происходит?
```
No. If we match the file to some descriptor `exec 4< ~/test.out`, delete the file and then read it from the descriptor `cat <&4` we get empty output.

If we are trying to read deleted file by its name we get an error.

Deletion of file is deletion of pointer to its inode and the file itself, if there is no hard links left.
```
