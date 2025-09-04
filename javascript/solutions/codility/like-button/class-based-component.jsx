import cx from 'classnames';
import { Component } from 'react';

export default class LikeButton extends Component {
    constructor(props) {
        super(props);
        this.state = {
            like_count_others: 100,
            current_user_has_liked: false,
        };
        this.onClickLike = this.onClickLike.bind(this)
    }

    onClickLike() {
        this.setState({
            ...this.state,
            current_user_has_liked: !this.state.current_user_has_liked,
        })
    }

    render() {
        let like_count = this.state.like_count_others
        if (this.state.current_user_has_liked) {
            like_count += 1
        }
        return (
            <>
                <div>
                    <h2>Like Button</h2>
                </div>
                <button
                    onClick={this.onClickLike}
                    className={cx({"like-button": true, "liked": this.state.current_user_has_liked })}
                >
                    {"Like | "}
                    <span className="likes-counter">{like_count}</span>
                </button>
                <style>{`
                    .like-button {
                        font-size: 1rem;
                        padding: 5px 10px;
                        color:  #585858;
                    }
                   .liked {
                        font-weight: bold;
                        color: #1565c0;
                   }
                `}</style>
            </>
        );
    }
}
