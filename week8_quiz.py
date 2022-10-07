attempts=open("answers.txt", "w")
attempts.write("1.D \n2.B \n3.B \n4.B \n5.D \n6.C \n7.C \n8.A \n9.A \n10.A \n11.D \n12.B \n13.A \n14.C \n15.C \n16.A \n17.D \n18.C \n19.D \n20.A \n21.B \n22.D \n23.B \n24.A \n25.B \n26.B \n27.A \n28.B \n29.A \n30.B \n31.A \n32.C \n33.D \n34.B \n35.A \n36.A \n37.B \n38.A \n39.B \n40.A")
attempts.close()

see_attempts=open("answers.txt", "r")
print(see_attempts.read())
see_attempts.close