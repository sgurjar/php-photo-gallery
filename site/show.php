<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
<title></title>
</head>
<body>
<?php
    $imgfile = htmlspecialchars($_GET['i']);
    if ($imgfile != ''){
        $path_parts = pathinfo($imgfile);
        echo "<h3>".$path_parts['filename']."</h3>";
        echo "<img src='$imgfile'>$imgfile</img>";
    }else {
        echo '<h3>click an image on left side to show here.</h3>';
    }
?>
</body>
</html>