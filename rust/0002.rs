struct Fib {
    curr: usize,
    next: usize,
}

impl Iterator for Fib {
    type Item = usize;

    fn next(&mut self) -> Option<usize> {
        let n = self.curr + self.next;
        self.curr = self.next;
        self.next = n;
        return Some(self.curr);
    }
}


fn main() {
    println!("The answer is {}", Fib {curr:1, next:2}
             .take_while(|&x| x < 4000000)
             .filter(|x| x % 2 == 0)
             .fold(0, |sum, x| {sum + x}));
}
