# Headers

### Accept

```
tells the format to send/recive
type/subtype [q=qvalue]
text/plain; q=0.5,text/html,text/x-div;q=0.8
```

### Accept-Charset

```
tells the character-set to send/recive
type [q=qvalue]
iso-8859-5; unicode-1-1;q-0.8
```

### Accept-Encoiding

```
tells the compression format to use
format;[q=qvalue]
gzip;q=1.0
```

### Accept-Language

```
tells the compression to user
lang;[q=qvalue]
en-gb;q=0.8
```

### Authorization

```
tells the compression to user
the format vary from service provider to provider
```

### Proxy-Authorization

```
tells the compression to user
the format vary from service provider to provider
```

### Cookie

```
helps to store value on client browser
```

### Expect

```
if the headers is large we send this to the server before sending the main request
100-continue
```

### If-Match

```
Cake.jpg=kmq13a
if-match : "kmq13a"
```

### If-None-Match Header

```
Cake.jpg=kmq13a
if-match : "kmq13a"
```
