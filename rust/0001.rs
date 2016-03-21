fn main() {
    let r = (1..1000)
        .filter(|n| (n % 3 == 0) | (n % 5 == 0))
        .fold(0, |sum, i| sum + i);
    println!("The answer is {}", r)
}
