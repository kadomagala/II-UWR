using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace _2._1._1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            MessageBox.Show(textBox1.Text + "\n" + textBox2.Text + "\n" + comboBox1.Text + "\n" + (checkBox1.Checked ? checkBox1.Text + "\n" : "") + (checkBox2.Checked ? checkBox1.Text + "\n" : ""));
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
