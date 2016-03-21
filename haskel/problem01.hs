xs = [x | x  <- [1..999], x `mod` 3 == 0 || x `mod` 5 == 0]
sum_of_xs = sum xs

main = do
    putStrLn $ show $ sum_of_xs
