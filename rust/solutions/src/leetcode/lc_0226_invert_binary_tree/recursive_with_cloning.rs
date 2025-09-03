use std::cell::RefCell;
use std::rc::Rc;

use crate::leetcode::lc_0226_invert_binary_tree::structs::TreeNode;

pub struct Solution;

impl Solution {
    pub fn invert_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        return match root {
            Some(tree_node_rc) => {
                match tree_node_rc.try_borrow_mut() {
                    Ok(mut tree_node) => {
                        let new_left = Self::invert_tree(tree_node.right.clone());
                        tree_node.right = Self::invert_tree(tree_node.left.clone());
                        tree_node.left = new_left;
                    }
                    Err(_) => todo!(),
                }
                return Some(tree_node_rc);
            }
            None => None,
        };
    }
}

pub type RecursiveWithCloningSolution = Solution;
