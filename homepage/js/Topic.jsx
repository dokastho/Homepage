import PropTypes from 'prop-types';
import React from 'react'
import Group from './Group';
import Scroller from './Scroller'

class Topic extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      name: "",
      groups: {},
      focusedGroupId: 0
    }
    this.groupScroll = this.groupScroll.bind(this);
  }

  componentDidMount() {
    const { name, groups } = this.props.content;
    const orderedGroupKeys = Object.keys(groups).map((key) => {
      const group = groups[key]
      return ({ id: key, groupOrder: group.groupOrder });
    }).sort((a, b) => a.groupOrder - b.groupOrder);
    this.setState({ name, groups, focusedGroupId: orderedGroupKeys[0].id });
  }

  groupScroll(direction) {
    const { focusedGroupId, groups } = this.state;
    const groupsKeys = Object.keys(groups);
    const focusedGroupIdx = groupsKeys.indexOf(focusedGroupId);
    if (direction === "up") {
      if (focusedGroupIdx === 0) {
        return;
      }
      const newFocusedGroupId = groupsKeys[focusedGroupIdx - 1]
      this.setState({ focusedGroupId: newFocusedGroupId });
    } else if (direction === "down") {
      if (focusedGroupIdx === groupsKeys.length - 1) {
        return;
      }
      const newFocusedGroupId = groupsKeys[focusedGroupIdx + 1]
      this.setState({ focusedGroupId: newFocusedGroupId });
    }
  }

  render() {
    const {
      topicIdx,
      content,
    } = this.props;

    const { name, groups, focusedGroupId } = this.state;
    const focusedGroup = groups[focusedGroupId];

    // apply styles
    const { styles } = content;
    const pstyles = JSON.parse(styles);
    const vars = Object.keys(pstyles);
    vars.map((v) => {
      document.documentElement.style.setProperty(`--${v}`, pstyles[v]);
    })

    return (
      <div className='topic' key={`${topicIdx}-${focusedGroupId}`}>
        <Scroller onScroll={this.groupScroll} />
        {
          focusedGroup ? <Group content={focusedGroup} /> : null
        }
      </div>
    );
  }
}

Topic.propTypes = {
  // prop types go here
  content: PropTypes.object,
  topicIdx: PropTypes.number.isRequired,
  // methods:
};

Topic.defaultProps = {
  // default prop values go here if not required
};

export default Topic

