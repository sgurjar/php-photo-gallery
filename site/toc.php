<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
<title></title>
</head>
<body>
<?php
$img_file_ext = array('jpg','jpeg');
$img_dir      = 'img';
$thumb_dir    = 'img/th';

if ($handle = opendir($thumb_dir)) {

    while (false !== ($file = readdir($handle))) {

        if(!is_dir($file)){
            $file_ext = strtolower(substr(strrchr($file,'.'),1));

            if(in_array($file_ext, $img_file_ext, true)){
                $thumbpath = $thumb_dir . '/' . $file;
                $filepath = $img_dir . '/' . $file;
                echo "
<p><a href='show.php?i=$filepath' target='_content_'>
    <img style='border-style:solid;border-width:thin' src='$thumbpath'/>
</a></p>";
            }
        }
    }
    closedir($handle);
}
?>
</body>
</html>