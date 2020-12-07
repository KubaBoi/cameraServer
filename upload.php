<?php
$save = $_REQUEST["save"];

$fileName = "gallery/image" . date("Ymdgi") . ".png";
print_r($_FILES);
if ($save == "1"):
    move_uploaded_file($_FILES["file"]["tmp_name"],$fileName);
move_uploaded_file($_FILES["file"]["tmp_name"],$_FILES["file"]["name"]);

echo $_FILES["file"]["tmp_name"] . "\n";
echo $_FILES["file"]["name"] . "\n";
echo $fileName;

?>