## BankFast

This challenge combines ReDoS attack with multithreading bugs.

```python
def donate(account):
    # Before regex
    bank, _ = get_data(account)
    pattern = re.compile("^([a-zA-Z]+)*$")
    if not pattern.match(account):
        print("Invalid account name")
    # After regex
    _, flags = get_data(account)
    write_data(account, bank - 1, flags)
    print("Thank you for your donation!")
```
We note that the `donate` function fetches bank balance before fetching flags.  
We also note that the regex used is vulnerable to Regex DoS  
The final command is also executed after the other commands have completed.

### Plan of action
1. Create an "invalid" account `aaaaaaaaaaaaaa!` (balance 900, flags 0)
2. Donate once  
    - Race condition due to regex validation
3. Buy 9 flags (balance 0, flags 9)
4. Regex validation completes, set balance to 899 but flags to 9
5. Buy final flag

**Input**
```
Account: aaaaaaaaaaaaaaaaaa!
Commands: donate,buy,buy,buy,buy,buy,buy,buy,buy,buy,buy
```
