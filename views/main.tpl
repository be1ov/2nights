<!DOCTYPE html>
<html>
<head>
    <title>{{f"{page_title} – " if page_title else ""}}{{app_title}}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
</head>
<body>
% include('header.tpl')
% include('content.tpl')
</body>
</html>