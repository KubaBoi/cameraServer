<?php
$uri = $_SERVER['REQUEST_URI'];
echo "\n";
echo $uri . "\n";
$save = explode("=", $uri )[1];

$fileName = "gallery/image" . date("Ymdgi") . ".png";
print_r($_FILES);
move_uploaded_file($_FILES["file"]["tmp_name"], $_FILES["file"]["name"]);

if ($save == 1) {
    echo "Saving\n";
    move_uploaded_file($_FILES["file"]["tmp_name"], $fileName);
    if (file_exists($fileName)) {
        echo "Saved\n";
    }
} else {
    echo "Not Saving\n";
}

print_r(scandir("gallery"));

echo $_FILES["file"]["tmp_name"] . "\n";
echo $_FILES["file"]["name"] . "\n";
echo $save . "\n";
echo $fileName;

?>