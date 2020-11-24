## JS Weird

Express supports [passing array and objects](https://masteringjs.io/tutorials/express/query-parameters) in query parameters.

### JS Weird 1
The first condition that needs to be satisfied is `a.length != a.toString().length`.  
In JavaScript, `Array.toString()` returns the elements joined by `,`. Alternatively, an object can be passed, which `toString()`s to `[object Object]`.


The second condition is that  `b.lol == 10`. This can be simply accomplished by passing `{lol: 10}`.


Query string: `?a[0]=1&a[1]=1&b[lol]=10`

### JS Weird 2

The first block executed is
```js
if (!(req.query.flag = "give flag")) {
  res.end(flag2)
  return;
}
```
There is a bug in the code: the assignment operator was used instead of `==`.  
Since `"give flag"` is truthy, the block will never be executed. However, `req.query.flag` will be set to `"give flag"`.


Next, the code checks if `req.query.flag.length + req.query.give.length + req.query.please` is equal to 420.
Since `req.query.flag` is known, we know `req.query.flag.length` is 9. However, express does not parse integers by default,
so `req.query.please` is a string. Since the minimum value of `req.query.flag.length + req.query.give.length` is 9,
`req.query.please` must be `0` to make `"420"`. Therefore, the length of `req.query.give` must be `42-9 = 33`.

Finally, `req.query.flag + req.query.give + req.query.please` must have length 69. We know that `req.query.flag.length + req.query.please.length = 10`.
Therefore, `req.query.give.toString()` must have length 59. We know it has 33 elements, which would produce 32 commas.
Hence, a valid `give` would have an element of `59-32 = 27` characters and 32 empty elements.

Query string:
```
give=0abcdefghijklmnopqrstuvwxyz&give=&give=&give=&give=&give=&give=&give=&give=&give=&give=&give=&give=&give=&give=&give=&give=&give=&give=&give=&give=&give=&give=&give=&give=&give=&give=&give=&give=&give=&give=&give=&give=&please=0
```
