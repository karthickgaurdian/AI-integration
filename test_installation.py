#!/usr/bin/env python
"""
Simple script to test if the AI E-commerce Assistant is installed correctly.
"""

try:
    # Try to import the package
    from ai_ecommerce_assistant import AIEcommerceAssistant
    print("✅ Successfully imported AIEcommerceAssistant")
    
    # Try to initialize the assistant
    assistant = AIEcommerceAssistant()
    print("✅ Successfully initialized AIEcommerceAssistant")
    
    # Try to access a method
    recommendations = assistant.get_recommendations(
        user_id="test_user",
        product_id="test_product",
        limit=1
    )
    print("✅ Successfully called get_recommendations method")
    print(f"Recommendations: {recommendations}")
    
    print("\n🎉 Installation test successful! The AI E-commerce Assistant is working correctly.")
    
except ImportError as e:
    print(f"❌ Error importing AIEcommerceAssistant: {e}")
    print("Make sure you've installed the package with 'pip install -e .'")
    
except Exception as e:
    print(f"❌ Error testing AIEcommerceAssistant: {e}")
    print("Check the error message above for details.") 