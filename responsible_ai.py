
def explain_prediction(message, prediction):
    print("\n=== Responsible AI Check ===")
    print("ML prediction:", prediction)

    print("\nLimitations:")
    print("- This model uses a very small demonstration dataset.")
    print("- A prediction can be incorrect.")
    print("- A normal-looking message can still be malicious.")
    print("- A suspicious-looking message can be legitimate.")

    print("\nPrivacy:")
    print("- Avoid entering real passwords, private messages, or personal data.")
    print("- Use anonymized or public test examples where possible.")

    print("\nRecommendation:")
    print("- Do not block an account based only on this model.")
    print("- Verify suspicious requests through an official channel.")
    print("- Treat the prediction as an initial signal, not proof.")

if __name__ == "__main__":
    sample_message = input("Enter a sample message: ").strip()
    sample_prediction = input("Enter its ML prediction: ").strip()

    explain_prediction(sample_message, sample_prediction)
