using System;
using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace _2._1._2
{



    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            progressBar1.BackColor = Color.Blue;
            progressBar1.ForeColor = Color.Yellow;

            ListViewItem li;

            li = listView1.Items.Add("John");
            li.SubItems.Add("Whick");
            li.SubItems.Add("35");

            li = listView1.Items.Add("Nick");
            li.SubItems.Add("Fury");
            li.SubItems.Add("34");

            li = listView1.Items.Add("Tom");
            li.SubItems.Add("Ridle");
            li.SubItems.Add("36");

            foreach (ColumnHeader ch in listView1.Columns)
                ch.Width = -2;

            listView1.ColumnClick += new ColumnClickEventHandler(LV_ColumnClick);
        }

        private void LV_ColumnClick(object sender, ColumnClickEventArgs e)
        {
            listView1.ListViewItemSorter = new MySorter(e.Column);
        }

        private void listView1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void progressBar1_Click(object sender, EventArgs e)
        {
            progressBar1.Value += 1;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            treeView1.Nodes.Add("Node 0");
            treeView1.Nodes.Add("Node 1");
            treeView1.Nodes.Add("Node 2");

            treeView1.Nodes[0].Nodes.Add("Subnode 0.0");
            treeView1.Nodes[0].Nodes.Add("Subnode 0.1");
            treeView1.Nodes[1].Nodes.Add("Subnode 1.0");
            treeView1.Nodes[2].Nodes.Add("Subnode 2.0");
            treeView1.Nodes[2].Nodes.Add("Subnode 2.1");
            treeView1.Nodes[2].Nodes.Add("Subnode 2.2");

            treeView1.Nodes[0].Nodes[0].Nodes.Add("Sub subnode 0.0.0");
            treeView1.Nodes[0].Nodes[0].Nodes.Add("Sub subnode 0.0.1");
        }

        List<TreeNode> checkedNodes = new List<TreeNode>();
        void removeChecked(TreeNodeCollection nodes)
        {
            foreach(TreeNode node in nodes)
            {
                if (node.Checked)
                {
                    checkedNodes.Add(node);
                }
                else
                {
                    removeChecked(node.Nodes);
                }
            }
            foreach(TreeNode checkedNode in checkedNodes)
            {
                nodes.Remove(checkedNode);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            removeChecked(treeView1.Nodes);
        }
    }
    public class MySorter : IComparer
    {
        int column;

        public MySorter(int column)
        {
            this.column = column;
        }

        public int Compare(object x, object y)
        {
            ListViewItem l1 = x as ListViewItem;
            ListViewItem l2 = y as ListViewItem;

            return string.Compare(l1.SubItems[column].Text, l2.SubItems[column].Text);
        }
    }
}
