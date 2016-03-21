fn main() {
    let mut ret = 0;
    for n in 1..1000 {
        if (n % 3 == 0) | (n % 5 == 0) {
            ret += n;
        }
    }
    println!("The answer is {}", ret);
}
