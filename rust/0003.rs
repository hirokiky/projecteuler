// #![feature(step_by)]

fn is_prime(x: usize) -> bool {
    match x {
        0 => false,
        1 => false,
        2 => true,
        i if i % 2 == 0 => false,
        i => !(3..i).filter(|x| x % 2 != 0)
            .any(|x| i % x == 0),
    }
}

fn factor(target:usize) -> Vec<usize> {
    let mut v = vec![];
    for n in (2..target+1)
        .filter(|x| is_prime(*x))
        .filter(|x| target % x == 0) {
            v.push(n);
            let c = v.iter().fold(1, |m, i| m * i);
            if c >= target {
                return v;
            }
        }
    return v;
}


#[test]
fn test_is_prime() {
    assert_eq!(is_prime(3), true);
    assert_eq!(is_prime(4), false);
    assert_eq!(is_prime(7), true);
    assert_eq!(is_prime(8), false);
    assert_eq!(is_prime(13), true);
    assert_eq!(is_prime(887), true);
}

#[test]
fn test_factor() {
    assert_eq!(factor(2), vec![2]);
    assert_eq!(factor(3), vec![3]);
    assert_eq!(factor(6), vec![2, 3]);
    assert_eq!(factor(8), vec![2]);
    assert_eq!(factor(13195), vec![5, 7, 13, 29]);
}


fn main() {
    println!("The answer is {}", factor(600851475143).last().unwrap());
}
