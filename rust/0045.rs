fn main() {
    let l = 100000;
    let triangles = (1..).map(|n| (n * (n + 1)) / 2);
    let pentagonals = (1..).map(|n| n * (3 * n - 1) / 2).take(l).collect::<Vec<u64>>();
    let hexagonals = (1..).map(|n| n * (2 * n - 1)).take(l).collect::<Vec<u64>>();

    let mut r = vec![];
    for n in triangles.take(l) {
        match pentagonals.binary_search(&n) {
            Ok(n) => n,
            Err(_) => continue,
        };
        match hexagonals.binary_search(&n) {
            Ok(n) => n,
            Err(_) => continue,
        };
        r.push(n);
        if r.len() >= 3 {
            break;
        };
    }
    println!("{:?}", r);
}

