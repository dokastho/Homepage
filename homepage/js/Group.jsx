import PropTypes from 'prop-types';
import React from 'react'
import Image from './Image';
import Story from './Story';

class Group extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      // state attributes go here
      stories: [],
      groupOrder: 0,
    };
  }

  componentDidMount() {
    const { content } = this.props;
    const { stories, groupOrder } = content;
    this.setState({ stories, groupOrder });
  }

  render() {
    const { stories, groupOrder } = this.state;
    return (
      <div className='group' key={groupOrder}>
        {
          stories.map((story, i) => {
            return (story.type === "media" ? <Image id={story.uuid} keyNum={i} /> : <Story text={story.text} keyNum={i} />)
          })
        }
      </div>
    );
  }
}

Group.propTypes = {
  // prop types go here
  content: PropTypes.instanceOf(Object).isRequired
};

Group.defaultProps = {
  // default prop values go here if not required
};

export default Group
