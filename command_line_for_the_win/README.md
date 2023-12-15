Command Line Challenge

Steps to use sftp
1. Open sandbox in alx dashboard
2. Copy ssh credentials by clicking on the SSH button
   This includes name@hostname
3. On the host machine (mine was Windows 10), navigate to the folder that
   contains the screenhots.
   It is from this folder that the files shall be copied using 'put'
4. Enter the command sftp name@hostname
5. After the password prompt: copy and paste the password from the sandbox menu
6. Now the prompt: 'sftp>' appears
7. Navigate to the directory within sandbox where the screenshots are to be put,
   mkdir where necessary
8. enter 'put -r ./'
   This command tells sftp to copy all the files in the current folder on the host
   machine into the folder currently navigated to 
   (in this case "/root/alx-system_engineering-devops/command_line_for_the_win/")
 9. ls to ensure that the files have been uploaded.
