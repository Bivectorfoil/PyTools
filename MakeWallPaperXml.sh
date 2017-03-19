#!/bin/bash

#How to use:
#生成控制ubuntu下的壁纸切换xml文件，files为下载的壁纸的路径,具体请搜索 ubuntu，shell,壁纸切换等关键字
#调用系统命令生成壁纸名
files=`ls -U /usr/share/backgrounds | grep -v contest`
last_file="empty"

echo '<background>'
echo '<starttime>'
echo '<year>2017</year>'
echo '<month>03</month>'
echo '<day>19</day>'
echo '<hour>11</hour>'
echo '<minute>40</minute>'
echo '<second>00</second>'
echo '</starttime>'

for current_file in $files
    do
        if [[ $last_file == "empty" ]]
        then
            last_file=$current_file
            echo '   <static>'
            echo '     <duration>7200.0</duration>'
            echo "     <file>/usr/share/backgrounds/$last_file</file>"
            echo '   </static>'
        else
            echo '   <transition>'
            echo '     <duration>5.0</duration>'
            echo "     <from>/usr/share/backgrounds/$last_file</from>"
            echo "     <to>/usr/share/backgrounds/$current_file</to>"
            echo '   </transition>'
            echo '   <static>'
            echo '     <duration>7200.0</duration>'
            echo "     <file>/usr/share/backgrounds/$current_file</file>"
            echo '  </static>'
            last_file=$current_file
        fi
    done

echo '</background>'
