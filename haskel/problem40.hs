import Data.Char

c = concat $ map show [1..]
gs f n = n : gs f (f n)

main = putStrLn $ show $ foldl (*) 1 $ map (digitToInt . (c !!) . (subtract 1)) $ take 7 $ gs (*10) 1