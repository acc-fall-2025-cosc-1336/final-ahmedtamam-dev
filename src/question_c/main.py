from question_c import (
    get_most_likely_ancestor_consensus,
    validate_dna_string,
    validate_dna_substring
)


def main():
    while True:
        print("\nDNA Substring Locator\n")

        # --- Get DNA string (8 < length <= 16) ---
        while True:
            dna1 = input("Enter a DNA string (length 9–16): ").upper()
            if validate_dna_string(dna1):
                break
            print("Invalid input. Try again.")

        # --- Get substring (length == 4) ---
        while True:
            dna2 = input("Enter a DNA substring of exactly 4 characters: ").upper()
            if validate_dna_substring(dna2):
                break
            print("Invalid input. Try again.")

        # --- Call the function ---
        results = get_most_likely_ancestor_consensus(dna1, dna2)

        # --- Display ---
        print("\nLocations:", *results)

        # --- Continue? ---
        again = input("\nRun again? (y/n): ").lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()