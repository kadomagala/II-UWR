using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace BasicWPFUI
{
    /// <summary>
    /// Logika interakcji dla klasy MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            string name = this.textBoxName.Text;
            string adress = this.textBoxAdress.Text;
            string cycle = this.comboBoxCycle.Text;
            string type = "";
            if (this.checkBoxDzienne.IsChecked.Equals(true))
            {
                type += checkBoxDzienne.Content+" ";
            }
            if (this.checkBoxUzup.IsChecked.Equals(true))
            {
                type += checkBoxUzup.Content;
            }
            MessageBox.Show(name + "\n" + adress + "\n" + cycle + "\n" + type);
        }

        private void Button_Click_1(object sender, RoutedEventArgs e)
        {
            Close();
        }
    }
}
