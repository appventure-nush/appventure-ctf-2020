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

#### JS Weird 3

This challenge was inspired by my own difficulties with JavaScript's `map` and `forEach` functions.  

The Map constructor takes an array of key-value pairs.
```javascript
const meep = new Map(JSON.parse(req.query.o));
```
However, JS's `forEach` on maps takes a `(value, key) => void` function rather than a `(key, value) => void` function, so the code below actually swaps the keys and values of the map.  
```javascript
meep.forEach((key, val) => {
  dict[key] = val;
});
```
The keys (the original values of the map) are then sorted and parsed as integers.
```js
const keys = Object.keys(dict).sort();
const ints = keys.filter(x => parseInt(x)).map(parseInt);
```
JS's map function takes a `(value, index) => result` function, where the index parameter can be omitted.  
In the case of `parseInt`, the second parameter is actually the base, ie `parseInt("1111",2) == 15`.  
Therefore, the first integer (index 0) parses as base 10 (default) while the rest parse as base-index.  
This allows us to generate `NaN`s in the ints array, which will be useful later.  

The strings are processed separately and joined with the ints. No surprises here.
```js
const string = keys.filter(x => !parseInt(x)).filter(x => x.length < 3).concat(ints).join("").split("");
```
This code simply deletes every third character from the string.
```js
string.forEach((a, b) => {
  if (parseInt(b) % 3 != 2) {
    out += a
  }
});
```
And the end result has to equal "banana".
```js
out.toLowerCase() === "banana"
```
It is impossible that "ba" would come from the `NaN`s, so it must be part of the strings array.  
We notice that there are no numbers in the end result, so they must have been eliminated by the third character deletion.
```
baXnaXnaX
```
We can now somewhat observe the pattern:
```
baXNaNNaN
```
This can be made by setting ints to an array of 3 single digit numbers, which would be parsed into `[X, NaN, NaN]`.
It is important they are unique so the dictionary keys won't be overwritten. The numbers should also be greater than their index.

Final query string:
```
?o=[["a","ba"],["b",1],["c",2],["d",3]]
```
