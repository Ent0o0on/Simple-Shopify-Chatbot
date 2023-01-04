import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QLabel, QVBoxLayout, QTextEdit
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt

class FAQBot(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()
    
  def initUI(self):
    self.layout = QVBoxLayout(self)
    
    self.question_prompt = QLineEdit(self)
    self.question_prompt.setPlaceholderText("Enter your question about Shopify")
    self.layout.addWidget(self.question_prompt)
    
    self.answer_paragraph = QTextEdit(self)
    self.answer_paragraph.setReadOnly(True)
    self.answer_paragraph.setFont(QFont("Arial", 10))
    self.layout.addWidget(self.answer_paragraph)
    
    self.question_prompt.returnPressed.connect(self.getAnswer)
    
    self.setLayout(self.layout)
    self.setGeometry(50, 50, 512, 512)
    self.setWindowTitle("Shopify FAQ Bot")
    self.setAutoFillBackground(True)
    p = self.palette()
    p.setColor(self.backgroundRole(), QColor(500, 230, 200))
    self.setPalette(p)
    self.show()

  def getAnswer(self):
    user_input = self.question_prompt.text()
    
    if user_input.lower() == "what is shopify?":
      answer = "Shopify is a platform that allows you to create an online store to sell your products. It offers a range of features including payment processing, inventory management, and marketing tools."
      
    elif user_input.lower() == "how much does shopify cost? " :
      answer = "Shopify offers several pricing plans, ranging from $29 to $299 per month. The exact plan that is best for you will depend on the size and needs of your business."
      
    elif user_input.lower() == "how do I get started with shopify?":
      answer = "To get started with Shopify, you can sign up for"

      
    elif user_input.lower() == "can I use my own domain with shopify?":
      answer = "Yes, you can use your own domain with Shopify. Simply connect your domain to your Shopify store and it will be used as the primary domain for your online store."

    elif user_input.lower() == "Can I use Shopify to sell physical and digital products?":
      answer = "Yes, Shopify allows you to sell both physical and digital products. You can also sell services and memberships through your online store."

    elif user_input.lower() == "Does Shopify offer a mobile app for managing my store?":
      answer = "Yes, Shopify offers a mobile app for iOS and Android devices that allows you to manage your store on the go. You can track sales, fulfill orders, and update your products from your phone or tablet."

    elif user_input.lower() == "Can I customize the design of my online store with Shopify?":
      answer = "Yes, Shopify offers a wide range of customizable templates for your online store. You can choose a pre-designed theme or use the drag-and-drop website builder to create a custom design."

    elif user_input.lower() == "Does Shopify provide customer support?":
      answer = "Yes, Shopify provides customer support through email, live chat, and phone. You can also access a knowledge base and community forum for additional support."  

    elif user_input.lower() == "Can I accept multiple payment methods with Shopify?":
      answer = "Yes, Shopify allows you to accept a variety of payment methods including credit cards, PayPal, and Apple Pay. You can also add additional payment gateways through the Shopify app store."  

    elif user_input.lower() == "Does Shopify offer inventory management tools?":
      answer = "Yes, Shopify offers a range of inventory management tools including the ability to track stock levels, set low stock alerts, and create purchase orders."

    elif user_input.lower() == "Can I use Shopify to market my online store?":
      answer = "Yes, Shopify offers a range of marketing tools including email marketing, social media integration, and support for Google and Facebook advertising. You can also use the Shopify app store to add additional marketing tools."
      
    else:
      answer = "I'm sorry, I don't have an answer for that. Please try asking a different question."
      
    self.question_prompt.clear()
    self.answer_paragraph.setText(answer)

app = QApplication(sys.argv)
faq_bot = FAQBot()
sys.exit(app.exec_())
