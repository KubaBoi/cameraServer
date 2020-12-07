<?php
$fileName = "gallery/image" . date("Ymdgi") . ".png";
print_r($_FILES);
move_uploaded_file($_FILES["file"]["tmp_name"],$fileName);
move_uploaded_file($_FILES["file"]["tmp_name"],$_FILES["file"]["name"]);

echo $_FILES["file"]["tmp_name"] . "\n";
echo $_FILES["file"]["name"] . "\n";
echo $fileName;

?>