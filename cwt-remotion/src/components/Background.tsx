import React from 'react';
import { AbsoluteFill, staticFile } from 'remotion';

export const Background: React.FC<{ project: string; item: any }> = ({ project, item }) => {
  
  const imagePath = `content/${project}/images/${item.image}`;
  
  return (
    <AbsoluteFill>
      <img
        src={staticFile(imagePath)}
        style={{ width: '100%', height: '100%', objectFit: 'cover' }}
      />
    </AbsoluteFill>
  );
};