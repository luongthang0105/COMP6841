use std::{env, fs};

fn check_matching_last(desired_match: i32, real_hash: &String, fake_hash: &String) -> bool{
    &real_hash[real_hash.len()-desired_match as usize..] == &fake_hash[fake_hash.len()-desired_match as usize..]
}
fn find_matching(desired_match: i32, hash_of_real_file: String, fake_file: String) {
    let num_states = 1 << 30;
    // println!("{:?}", num_states);
    
    for state in 0..num_states {
        let fake_file = fake_file.clone();
        let fake_file = fake_file.lines().zip(0..).map(|(line, index)| {
            if (state >> index) & 1 == 1 {
                let mut new_str = String::from(line);
                new_str.push(' ');
                new_str.as_str().to_owned()
            } else {
                String::from(line)
            }
        });

        let new_fake_file = fake_file.collect::<Vec<String>>().join("\n");
        let hash_of_fake_file = sha256::digest(new_fake_file.clone());

        if check_matching_last(desired_match, &hash_of_real_file, &hash_of_fake_file) {
            println!("FOUND MATCHING STATE {state}!");
            fs::write("../result.txt", new_fake_file).expect("Should be able to write to file");
            return;
        }
    }
}

fn main() {
    let desired_match = env::args().nth(1).expect("Missing argument 1").parse::<i32>().expect("Expects a number");

    let real_file = fs::read_to_string("../confession_real.txt").unwrap();
    let fake_file = fs::read_to_string("../confession_fake.txt").unwrap();
    let hash_of_real_file = sha256::digest(real_file);

    find_matching(desired_match, hash_of_real_file, fake_file);
}
